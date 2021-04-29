#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hydra
import os


def get_root_path(path: str) -> str:
    root = hydra.utils.get_original_cwd()
    return os.path.join(root, path)
