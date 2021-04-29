from dataclasses import dataclass
from omegaconf import MISSING
from typing import Any


@dataclass
class EDAConfig:
    raw_data_path: str = MISSING
    report_dir: str = MISSING
    report_file_name: str = MISSING
    report_class: Any = MISSING


@dataclass
class PandasProfilingConfig:
    _target_: str = MISSING
    title: str = MISSING
    explorative: bool = MISSING


@dataclass
class ReportConfig(EDAConfig):
    report_class: PandasProfilingConfig = MISSING
