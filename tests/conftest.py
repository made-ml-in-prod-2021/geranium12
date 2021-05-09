#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from typing import cast

import pandas as pd
import pytest
from hydra.experimental import compose, initialize
from sklearn.svm import SVC

from ml_project.configs import Config
from ml_project.configs.split_config import SimpleSplitConfig
from ml_project.data import read_data
from tests.data.make_fake_dataset import make_fake_dataset
from tests.data.make_fake_test_dataset import make_fake_test_dataset


@pytest.fixture()
def dataset_path() -> str:
    path = os.path.join(os.path.dirname(__file__), "data/train.csv")
    data = make_fake_dataset()
    data.to_csv(path)
    return path


def test_dataset_path() -> str:
    path = os.path.join(os.path.dirname(__file__), "data/train.csv")
    data = make_fake_test_dataset()
    data.to_csv(path)
    return path


@pytest.fixture()
def target_column() -> str:
    return "target"


@pytest.fixture()
def dataset(dataset_path: str) -> pd.DataFrame:
    return read_data(dataset_path)


@pytest.fixture()
def split_config() -> SimpleSplitConfig:
    return SimpleSplitConfig(train_size=0.8)


@pytest.fixture()
def model_path() -> str:
    return os.path.join(os.path.dirname(__file__), "data/model.pkl")


@pytest.fixture()
def metric_path() -> str:
    return os.path.join(os.path.dirname(__file__), "data/metric.txt")


@pytest.fixture()
def preds_path() -> str:
    return os.path.join(os.path.dirname(__file__), "data/predictions.csv")


@pytest.fixture()
def test_data_path() -> str:
    return os.path.join(os.path.dirname(__file__), "data/train.csv")


@pytest.fixture()
def svm_model() -> object:
    return SVC()


@pytest.fixture()
def simple_config(
        model_path, dataset_path, target_column, metric_path, preds_path, test_data_path
) -> Config:
    try:
        initialize(config_path="../configs", job_name="test_app")
    except ValueError:
        pass
    cfg = compose(config_name="config", return_hydra_config=True)
    cfg = cast(Config, cfg)
    cfg.main.model_path = model_path
    cfg.main.raw_data_path = dataset_path
    cfg.main.target_column = target_column
    cfg.main.metric_path = metric_path
    cfg.main.preds_path = preds_path
    cfg.main.test_data_path = test_data_path
    return cfg
