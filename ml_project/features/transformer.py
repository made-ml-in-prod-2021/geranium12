import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.exceptions import NotFittedError
from typing import Tuple


class MinMaxTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.min = 0
        self.max = 0
        self.fitted = False

    def fit(self, data: pd.DataFrame):
        self.min = data.min()
        self.max = data.max()
        self.fitted = True
        return self

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        if not self.fitted:
            raise NotFittedError("MinMaxTransformer is not fitted!")

        return (data - self.min) / (self.max - self.min)
