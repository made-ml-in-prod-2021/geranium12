import pickle
import typing
from pathlib import Path
from typing import Tuple, NoReturn

import click
import pandas as pd
from sklearn import preprocessing
from sklearn.base import TransformerMixin


@click.command()
@click.option("--load_path", "-l", required=True)
@click.option("--save_path", "-s", required=True)
@click.option("--model_path", "-m", required=True)
def fit_transformer(load_path: str, save_path: str, model_path: str) -> NoReturn:
    data_train, data_test, targets_train, targets_test = load_data(
        Path(load_path)
    )
    scaler = typing.cast(
        preprocessing.StandardScaler, preprocessing.StandardScaler().fit(data_train)
    )
    data_train = pd.DataFrame(
        scaler.transform(data_train), columns=data_train.columns
    )
    data_test = pd.DataFrame(
        scaler.transform(data_test), columns=data_test.columns
    )
    save_data(
        Path(save_path),
        data_train,
        data_test,
        targets_train,
        targets_test,
    )
    save_transformer(Path(model_path), scaler)


def load_data(load_path: Path) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    data_train, data_test = [
        pd.read_csv(Path(load_path, f"{data_name}.csv"))
        for data_name in ["data_train", "data_test"]
    ]
    targets_train, targets_test = [
        pd.read_csv(Path(load_path, f"{data_name}.csv"), squeeze=True, dtype=int)
        for data_name in ["target_train", "target_test"]
    ]
    return data_train, data_test, targets_train, targets_test


def save_data(
        path: Path,
        data_train: pd.DataFrame,
        data_test: pd.DataFrame,
        targets_train: pd.Series,
        targets_test: pd.Series,
) -> NoReturn:
    for dataset, name in zip(
            [data_train, data_test, targets_train, targets_test],
            ["data_train", "data_test", "target_train", "target_test"],
    ):
        dataset.to_csv(Path(path, f"{name}.csv"), index=False)


def save_transformer(path: Path, transformer: TransformerMixin, ) -> NoReturn:
    with open(Path(path, "transformer.pickle"), "wb") as f:
        pickle.dump(transformer, f)


if __name__ == "__main__":
    fit_transformer()
