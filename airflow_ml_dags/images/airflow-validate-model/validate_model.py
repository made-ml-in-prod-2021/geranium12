import pickle
from pathlib import Path
from typing import Tuple, NoReturn

import click
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


@click.command()
@click.option("--data_path", "-d", required=True)
@click.option("--model_path", "-m", required=True)
def validate(data_path: str, model_path: str):
    data_test, target_test = load_data(Path(data_path))
    model = load_model(Path(model_path))
    preds = model.predict(data_test)
    report = classification_report(target_test, preds)
    save_metrics(report, Path(model_path))


def load_data(data_path: Path) -> Tuple[pd.DataFrame, pd.Series]:
    return (
        pd.read_csv(Path(data_path, "data_test.csv")),
        pd.read_csv(Path(data_path, "target_test.csv"), squeeze=True),
    )


def load_model(path: Path) -> LogisticRegression:
    with open(Path(path, "model.pickle"), "rb") as f:
        model = pickle.load(f)
    return model


def save_metrics(metrics: str, path: Path) -> NoReturn:
    with open(Path(path, "metrics.txt"), "w") as f:
        f.write(metrics)


if __name__ == "__main__":
    validate()
