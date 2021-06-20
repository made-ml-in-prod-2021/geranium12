import pickle
from pathlib import Path
from typing import NoReturn
from typing import Tuple

import click
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


@click.command()
@click.option("--data_path", "-d", required=True)
@click.option("--model_path", "-m", required=True)
@click.option("--predictions_path", "-p", required=True)
def predict(data_path: str, model_path: str, predictions_path: str) -> NoReturn:
    dataset = load_data(Path(data_path))
    model, transformer = load_model(Path(model_path))
    predictions = pd.Series(model.predict(transformer.transform(dataset)))
    save_predictions(predictions, Path(predictions_path))


def load_data(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(Path(data_path, "data.csv"))


def load_model(model_path: Path) -> Tuple[LogisticRegression, StandardScaler]:
    with open(Path(model_path, "model.pickle"), "rb") as f:
        model = pickle.load(f)
    with open(Path(model_path, "transformer.pickle"), "rb") as f:
        transformer = pickle.load(f)
    return model, transformer


def save_predictions(predictions: pd.Series, path: Path) -> NoReturn:
    predictions.to_csv(Path(path, "preds.csv"), index=False)


if __name__ == "__main__":
    predict()
