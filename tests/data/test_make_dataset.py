import pandas as pd
from ml_project.data import read_data, train_test_split
from ml_project.configs.split_config import SimpleSplitConfig


def test_read_data(dataset_path: str, target_column: str) -> None:
    data = read_data(dataset_path)
    assert len(data) > 20
    assert target_column in data.keys()


def test_train_test_split(
        dataset: pd.DataFrame, split_config: SimpleSplitConfig
) -> None:
    train_data, val_data = train_test_split(dataset, split_config)
    assert len(train_data) + len(val_data) == len(dataset)
