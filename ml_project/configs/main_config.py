#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class MainConfig:
    raw_data_path: str = MISSING
    eda_dir: str = MISSING
    metric_path: str = MISSING
    model_path: str = MISSING
    preds_path: str = MISSING
    test_data_path: str = MISSING
    target_column: str = MISSING
