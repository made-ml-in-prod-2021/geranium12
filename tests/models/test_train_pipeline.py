#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import pickle

from ml_project.configs import Config
from models.train_pipeline import train_pipeline


def test_train_pipeline(simple_config: Config) -> None:
    train_pipeline(simple_config)
    assert os.path.exists(simple_config.main.metric_path)
    assert os.path.exists(simple_config.main.model_path)
    with open(simple_config.main.metric_path, "r") as f:
        metrics = json.load(f)
        assert metrics["accuracy"] > 0
    with open(simple_config.main.model_path, "rb") as f:
        pipeline = pickle.load(f)
    assert "transform" in pipeline.keys()
    assert "model" in pipeline.keys()
