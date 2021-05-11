#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import pytest

from ml_project.configs.split_config import SimpleSplitConfig
from ml_project.data import read_data


@pytest.fixture(scope="function")
def dataset_path(tmpdir) -> str:
    path = tmpdir.mkdir("data").join("train.csv")
    data = make_fake_dataset()
    data.to_csv(path)
    return path


@pytest.fixture(scope="session")
def target_column() -> str:
    return "target"


@pytest.fixture(scope="function")
def dataset(dataset_path: str) -> pd.DataFrame:
    return read_data(dataset_path)


@pytest.fixture(scope="session")
def split_config() -> SimpleSplitConfig:
    return SimpleSplitConfig(train_size=0.8)


@pytest.fixture(scope="function")
def test_dataset(dataset_path: str, target_column: str) -> pd.DataFrame:
    return read_data(dataset_path).drop(target_column, axis=1)


def make_fake_dataset(size: int = 30, random_seed: int = 11) -> pd.DataFrame:
    np.random.seed(random_seed)
    data = pd.DataFrame()
    data["age"] = np.random.normal(loc=54, scale=9, size=size).astype(int)
    data["sex"] = np.random.binomial(n=1, p=0.7, size=size).astype(int)
    data["cp"] = np.random.randint(low=0, high=4, size=size).astype(int)
    data["trestbps"] = np.random.normal(
        loc=132, scale=18, size=size).astype(int)
    data["chol"] = np.random.normal(loc=246, scale=52, size=size).astype(int)
    data["fbs"] = np.random.binomial(n=1, p=0.7, size=size).astype(int)
    data["restecg"] = np.random.randint(
        low=0, high=3, size=size).astype(int)
    data["thalach"] = np.random.normal(
        loc=150, scale=23, size=size).astype(int)
    data["exang"] = np.random.binomial(n=1, p=0.7, size=size).astype(int)
    data["oldpeak"] = np.random.normal(
        loc=1, scale=1.16, size=size).astype(int)
    data["slope"] = np.random.randint(low=0, high=3, size=size).astype(int)
    data["ca"] = np.random.randint(low=0, high=5, size=size).astype(int)
    data["thal"] = np.random.randint(low=0, high=4, size=size).astype(int)
    data["target"] = np.random.binomial(n=1, p=0.7, size=size).astype(int)
    return data
