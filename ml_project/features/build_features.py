import pandas as pd
from typing import Tuple


def target_split(
    data: pd.DataFrame, target_column: str
) -> Tuple[pd.DataFrame, pd.Series]:
    return data.drop(target_column, axis=1), data[target_column]
