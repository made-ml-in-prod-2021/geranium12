from dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class ModelConfig:
    _target_: str = MISSING


@dataclass
class SVMConfig(ModelConfig):
    C: float = MISSING
    kernel: str = MISSING
    degree: int = MISSING


@dataclass
class KNNConfig(ModelConfig):
    n_neighbors: int = MISSING
