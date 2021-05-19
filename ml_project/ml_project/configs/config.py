#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from omegaconf import MISSING
from ml_project.configs.main_config import MainConfig
from ml_project.configs.eda_config import EDAConfig
from ml_project.configs.split_config import SplitConfig
from ml_project.configs.model_config import ModelConfig


@dataclass
class Config:
    main: MainConfig = MISSING
    eda: EDAConfig = MISSING
    split: SplitConfig = MISSING
    model: ModelConfig = MISSING
