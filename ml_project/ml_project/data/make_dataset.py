#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.config
from typing import Tuple

import pandas as pd
from sklearn import model_selection

from ml_project.configs.split_config import SimpleSplitConfig

logger = logging.getLogger(__name__)


def read_data(path: str) -> pd.DataFrame:
    logger.info("Started reading data...")
    data = pd.read_csv(path)
    logger.info("Finished reading data successfully!")
    return data


def train_test_split(
        data: pd.DataFrame, split_config: SimpleSplitConfig
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    logger.info("Started train test data splitting...")
    train, test = model_selection.train_test_split(
        data, train_size=split_config.train_size, random_state=11
    )
    logger.info("Finished train test data splitting!")
    return train, test
