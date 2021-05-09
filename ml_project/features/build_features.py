#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.config
from typing import Tuple

import pandas as pd

logger = logging.getLogger(__name__)


def target_split(
        data: pd.DataFrame, target_column: str
) -> Tuple[pd.DataFrame, pd.Series]:
    logger.info("Started target column dropping...")
    data_without_target = data.drop(target_column, axis=1), data[target_column]
    logger.info("Finished target column dropping!")
    return data_without_target
