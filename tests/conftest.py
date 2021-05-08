import os

import pandas as pd
import pytest

from ml_project.configs.split_config import SimpleSplitConfig
from tests.data.make_fake_dataset import make_fake_dataset
from ml_project.data import read_data
from ml_project.configs import Config


@pytest.fixture()
def dataset_path() -> str:
    path = os.path.join(os.path.dirname(__file__), "data/heart.csv")
    data = make_fake_dataset()
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
