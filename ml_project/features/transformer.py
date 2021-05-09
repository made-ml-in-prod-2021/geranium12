#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.config

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.exceptions import NotFittedError

logger = logging.getLogger(__name__)


class MinMaxTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.min = 0
        self.max = 0
        self.fitted = False
        logger.info("Created MinMaxTransformer!")

    def fit(self, data: pd.DataFrame):
        self.min = data.min()
        self.max = data.max()
        self.fitted = True
        logger.info("Fitted MinMaxTransformer!")
        return self

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        if not self.fitted:
            raise NotFittedError("MinMaxTransformer is not fitted!")
        transformed_data = (data - self.min) / (self.max - self.min)
        logger.info("MinMaxTransformer transformed data!")
        return transformed_data
