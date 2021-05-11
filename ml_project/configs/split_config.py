#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass

from omegaconf import MISSING


@dataclass
class SplitConfig:
    pass


@dataclass
class SimpleSplitConfig(SplitConfig):
    train_size: float = MISSING
