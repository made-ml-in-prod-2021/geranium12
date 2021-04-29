#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hydra
import pandas as pd
import os

from omegaconf import DictConfig
from ml_project.utils.utils import get_root_path
from pathlib import Path


@hydra.main(config_path="../../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    data = pd.read_csv(get_root_path(cfg.eda.raw_data_path))
    report = hydra.utils.instantiate(cfg.eda.eda_class, data)
    report_dir = get_root_path(cfg.eda.report_dir)
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    report.to_file(os.path.join(report_dir, cfg.eda.report_file_name))


if __name__ == "__main__":
    main()
