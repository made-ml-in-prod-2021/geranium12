import os

import pandas as pd
import pytest


from tests.data.make_fake_dataset import make_fake_dataset
from ml_project.data import read_data


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
