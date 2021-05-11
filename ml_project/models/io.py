#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.config
import pickle

from ml_project.utils import get_root_path

logger = logging.getLogger(__name__)


def load_model(path: str) -> object:
    logger.info("Loading model...")
    path = get_root_path(path)
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def save_model(model: object, path: str) -> str:
    logger.info("Saving model...")
    path = get_root_path(path)
    with open(path, "wb") as f:
        pickle.dump(model, f)
    return path
