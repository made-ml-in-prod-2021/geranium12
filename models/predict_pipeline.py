import pickle

import hydra
import pandas as pd

from ml_project.configs import Config
from ml_project.data import read_data
from ml_project.utils import get_root_path
from models.train_pipeline import predict_model


def load_model(path: str) -> object:
    path = get_root_path(path)
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def save_predictions(predictions: pd.DataFrame, path: str) -> str:
    path = get_root_path(path)
    predictions.to_csv(path, index=False)
    return path


def predict_pipeline(cfg: Config) -> None:
    pipeline = load_model(cfg.main.model_path)
    transformer = pipeline["transformer"]
    model = pipeline["model"]
    data = read_data(get_root_path(cfg.main.test_data_path))
    transformed_data = transformer.transform(data)
    predictions = predict_model(model, data)
    save_predictions(predictions, cfg.main.preds_path)


@hydra.main(config_path="../configs", config_name="config")
def main(cfg: Config):
    predict_pipeline(cfg)


if __name__ == "__main__":
    main()
