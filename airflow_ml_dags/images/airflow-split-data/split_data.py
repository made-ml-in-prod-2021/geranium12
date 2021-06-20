import os
from pathlib import Path
from typing import Tuple, NoReturn

import click
import pandas as pd
import sklearn.model_selection


@click.command()
@click.option("--load_path", "-l", required=True)
@click.option("--save_path", "-s", required=True)
@click.option("--train_ratio", "-t", default=0.8)
@click.option("--random_state", "-r", default=11)
def split_data(load_path: str, save_path: str, train_ratio: float, random_state: int) -> NoReturn:
    data, targets = load_data(Path(load_path))
    data_train, data_test, targets_train, targets_test = train_test_split(
        data, targets, train_ratio=train_ratio, random_state=random_state
    )
    save_data(
        Path(save_path), data_train, data_test, targets_train, targets_test
    )


def load_data(load_path: Path) -> Tuple[pd.DataFrame, pd.Series]:
    return (
        pd.read_csv(Path(load_path, "data.csv")),
        pd.read_csv(Path(load_path, "target.csv"), squeeze=True),
    )


def train_test_split(
        features: pd.DataFrame, targets: pd.Series, train_ratio: float, random_state: int
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    return sklearn.model_selection.train_test_split(
        features, targets, train_size=train_ratio, random_state=random_state
    )


def save_data(
        save_path: Path,
        features_train: pd.DataFrame,
        features_test: pd.DataFrame,
        targets_train: pd.Series,
        targets_test: pd.Series,
) -> NoReturn:
    os.makedirs(save_path, exist_ok=True)
    for dataset, name in zip(
            [features_train, features_test, targets_train, targets_test],
            ["data_train", "data_test", "target_train", "target_test"],
    ):
        dataset.to_csv(Path(save_path, f"{name}.csv"), index=False)


if __name__ == "__main__":
    split_data()
