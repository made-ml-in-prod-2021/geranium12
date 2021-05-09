#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from ml_project.configs import Config
from ml_project.data import read_data
from ml_project.utils import get_root_path
from models.predict_pipeline import predict_pipeline


def test_predict_pipeline(simple_config: Config) -> None:
    predict_pipeline(simple_config)
    assert os.path.exists(simple_config.main.preds_path)
    predictions = read_data(get_root_path(simple_config.main.preds_path))
    data = read_data(get_root_path(simple_config.main.test_data_path))
    assert len(predictions) == len(data)
