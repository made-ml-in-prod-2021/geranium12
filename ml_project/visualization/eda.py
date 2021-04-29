#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hydra
import os

from pathlib import Path
from ml_project.configs import Config
from ml_project.utils.utils import get_root_path
from ml_project.data.make_dataset import read_data


@hydra.main(config_path="../../configs", config_name="config")
def main(cfg: Config) -> None:
    data = read_data(get_root_path(cfg.eda.raw_data_path))
    report = hydra.utils.instantiate(cfg.eda.report_class, data)
    report_dir = get_root_path(cfg.eda.report_dir)
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    report.to_file(os.path.join(report_dir, cfg.eda.report_file_name))


if __name__ == "__main__":
    main()
