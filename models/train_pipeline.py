import json
import pickle
import typing
from typing import Dict
from typing import Union

import hydra
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

from ml_project.configs import Config
from ml_project.configs.split_config import SimpleSplitConfig
from ml_project.data import read_data, train_test_split
from ml_project.features import target_split, MinMaxTransformer
from ml_project.utils import get_root_path

SklearnModel = Union[SVC, KNeighborsClassifier]


def train_model(features: pd.DataFrame, target: pd.Series, cfg: Config) -> SklearnModel:
    model = hydra.utils.instantiate(cfg.model).fit(features, target)
    return model


def predict_model(model: SklearnModel, features: pd.DataFrame) -> pd.DataFrame:
    predicts = model.predict(features)
    return pd.DataFrame(predicts)


def evaluate_model(
    model: SklearnModel, features: pd.DataFrame, target: pd.Series
) -> Dict[str, float]:
    return {
        "accuracy": model.score(features, target),
    }


def make_pipeline(model: SklearnModel, transformer: MinMaxTransformer) -> Pipeline:
    return Pipeline([("transformer", transformer), ("model", model)])


def save_metrics(metrics: Dict, path: str) -> str:
    path = get_root_path(path)
    with open(path, "w") as f:
        json.dump(metrics, f)
    return path


def save_model(model: object, path: str) -> str:
    path = get_root_path(path)
    with open(path, "wb") as f:
        pickle.dump(model, f)
    return path


def train_pipeline(cfg: Config) -> None:
    data = read_data(get_root_path(cfg.main.raw_data_path))
    train_data, val_data = train_test_split(
        data, typing.cast(SimpleSplitConfig, cfg.split)
    )

    train_features, train_target = target_split(train_data, cfg.main.target_column)
    val_features, val_target = target_split(val_data, cfg.main.target_column)

    transformer = MinMaxTransformer().fit(train_features)
    train_features = transformer.transform(train_features)
    val_features = transformer.transform(val_features)

    model = train_model(train_features, train_target, cfg)
    pipeline = make_pipeline(model, transformer)
    val_predictions = predict_model(pipeline, val_features)
    metrics = evaluate_model(model, val_features, val_target)

    save_metrics(metrics, cfg.main.metric_path)
    save_model(pipeline, cfg.main.model_path)


@hydra.main(config_path="../configs", config_name="config")
def main(cfg: Config):
    train_pipeline(cfg)


if __name__ == "__main__":
    main()
