#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.config

import hydra
import pandas as pd

from ml_project.configs import Config
from ml_project.data import read_data
from ml_project.models.io import load_model
from ml_project.models.train_pipeline import predict_model
from ml_project.utils import get_root_path

logger = logging.getLogger(__name__)


def save_predictions(predictions: pd.DataFrame, path: str) -> str:
    logger.info("Predicting data...")
    path = get_root_path(path)
    predictions.to_csv(path, index=False)
    return path


def predict_pipeline(cfg: Config) -> None:
    logger.info("Predict pipeline has started!")
    pipeline = load_model(cfg.main.model_path)
    transformer = pipeline["transformer"]
    model = pipeline["model"]
    data = read_data(get_root_path(cfg.main.test_data_path))
    transformed_data = transformer.transform(data)
    predictions = predict_model(model, transformed_data)
    save_predictions(predictions, cfg.main.preds_path)
    logger.info("Predict pipeline has finished!")


@hydra.main(config_path="../../configs", config_name="config")
def main(cfg: Config):
    predict_pipeline(cfg)


if __name__ == "__main__":
    main()
