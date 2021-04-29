#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hydra.core.config_store import ConfigStore

from .config import Config
from .eda_config import ReportConfig
from .main_config import MainConfig


cs = ConfigStore.instance()
# cs.store(group="schema/eda", name="eda", node=ReportConfig, package="eda")
# cs.store(group="schema/main", name="main", node=MainConfig, package="main")
cs.store(name="config", node=Config)


__all__ = ["Config"]
