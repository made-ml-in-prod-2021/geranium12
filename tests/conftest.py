import pytest
import os


from data.make_fake_dataset import make_fake_dataset


@pytest.fixture()
def dataset_path():
    path = os.path.join(os.path.dirname(__file__), "data/heart.csv")
    data = make_fake_dataset()
    data.to_csv(path)
    return path


@pytest.fixture()
def target_column():
    return "target"
