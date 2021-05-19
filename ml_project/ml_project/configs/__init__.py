#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hydra.core.config_store import ConfigStore

from ml_project.configs.config import Config
from ml_project.configs.eda_config import PandasProfilingConfig
from ml_project.configs.main_config import MainConfig
from ml_project.configs.split_config import SplitConfig, SimpleSplitConfig
from ml_project.configs.model_config import KNNConfig
from ml_project.configs.model_config import SVMConfig


cs = ConfigStore.instance()
cs.store(group="main", name="main", node=MainConfig)
cs.store(group="eda", name="eda", node=PandasProfilingConfig)
cs.store(group="split", name="split_config", node=SimpleSplitConfig)
cs.store(group="model", name="knn_config", node=KNNConfig)
cs.store(group="model", name="svm_config", node=SVMConfig)
cs.store(name="config", node=Config)

__all__ = ["Config", "SimpleSplitConfig", "SplitConfig"]
