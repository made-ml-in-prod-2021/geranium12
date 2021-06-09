import pickle
from pathlib import Path
from typing import Tuple
from typing import NoReturn

import click
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression


@click.command()
@click.option("--data_path", "-d", required=True)
@click.option("--model_path", "-m", required=True)
@click.option("--random_state", "-r", default=11)
def fit_model(data_path: str, model_path: str, random_state: int = 11) -> NoReturn:
    data_train, target_train = load_data(Path(data_path))
    model = LogisticRegression(random_state=random_state).fit(data_train, target_train)
    save_model(model, Path(model_path))


def load_data(data_path: Path) -> Tuple[pd.DataFrame, pd.Series]:
    return (
        pd.read_csv(Path(data_path, "data_train.csv")),
        pd.read_csv(Path(data_path, "target_train.csv"), squeeze=True, dtype=int),
    )


def save_model(model: BaseEstimator, path: Path) -> NoReturn:
    with open(Path(path, "model.pickle"), "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    fit_model()
