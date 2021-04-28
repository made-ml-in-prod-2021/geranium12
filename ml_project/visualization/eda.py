#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hydra
import pandas as pd
import os

from omegaconf import DictConfig
from pandas_profiling import ProfileReport
from ml_project.utils.utils import get_root_path
from pathlib import Path


@hydra.main(config_path="../../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    report_dir = get_root_path(cfg.eda.report_dir)
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    ProfileReport(
        pd.read_csv(get_root_path(cfg.eda.raw_data_path)), explorative=True
    ).to_file(os.path.join(report_dir, cfg.eda.report_file_name))


if __name__ == "__main__":
    main()
