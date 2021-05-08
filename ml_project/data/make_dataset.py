#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import model_selection
from ml_project.configs.split_config import SimpleSplitConfig
from typing import Tuple


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def train_test_split(
    data: pd.DataFrame, split_config: SimpleSplitConfig
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return model_selection.train_test_split(
        data, train_size=split_config.train_size, random_state=11
    )
