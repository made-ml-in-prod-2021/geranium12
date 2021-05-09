#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.config
import os
from pathlib import Path

import hydra

from ml_project.configs import Config
from ml_project.data.make_dataset import read_data
from ml_project.utils.utils import get_root_path

logger = logging.getLogger(__name__)


@hydra.main(config_path="../../configs", config_name="config")
def main(cfg: Config) -> None:
    logger.info("Reading data...")
    data = read_data(get_root_path(cfg.eda.raw_data_path))
    report = hydra.utils.instantiate(cfg.eda.report_class, data)
    report_dir = get_root_path(cfg.eda.report_dir)
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    logger.info("Creating report with pandas_profiling...")
    report.to_file(os.path.join(report_dir, cfg.eda.report_file_name))


if __name__ == "__main__":
    main()
