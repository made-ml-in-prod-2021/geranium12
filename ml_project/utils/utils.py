#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hydra
import os


def get_root_path(path):
    root = hydra.utils.get_original_cwd()
    return os.path.join(root, path)
