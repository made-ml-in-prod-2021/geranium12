#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class MainConfig:
    raw_data_path: str = MISSING
    eda_dir: str = MISSING
