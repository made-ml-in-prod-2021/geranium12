import os
from pathlib import Path

import click
import numpy as np
import pandas as pd


@click.command()
@click.option("--save_path", "-s", required=True)
@click.option("--size", default=100)
@click.option("--random_state", "-r", default=11)
def download_data(save_path: str, size: int, random_state: int) -> None:
    data = make_fake_dataset(size=size, random_state=random_state)
    targets = data["target"]
    data = data.drop("target", axis=1)
    save_data(save_path, data, targets)


def save_data(save_path: str, data: pd.DataFrame, targets: pd.Series) -> None:
    os.makedirs(save_path, exist_ok=True)
    data.to_csv(Path(save_path, "data.csv"), sep=",")
    targets.to_csv(Path(save_path, "target.csv"), sep=",", index=False)


def make_fake_dataset(size: int = 30, random_state: int = 11) -> pd.DataFrame:
    np.random.seed(random_state)
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


if __name__ == "__main__":
    download_data()
