import pandas as pd

from ml_project.features import MinMaxTransformer
from ml_project.features import target_split


def test_minmaxtransformer(dataset: pd.DataFrame, target_column: str):
    data, target = target_split(dataset, target_column)
    transformer = MinMaxTransformer()
    transformer.fit(data)
    transformed_data = transformer.transform(data)
    assert type(transformed_data) == pd.DataFrame
    assert len(transformed_data) == len(data)
    assert all(transformed_data.max() == 1)
    assert all(transformed_data.min() == 0)
