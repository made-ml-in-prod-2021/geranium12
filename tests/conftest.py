#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import pandas as pd
import pytest

from ml_project.configs.split_config import SimpleSplitConfig
from ml_project.data import read_data
from tests.data.make_fake_dataset import make_fake_dataset


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
