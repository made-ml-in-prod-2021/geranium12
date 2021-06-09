import sys

import pytest
from airflow.models import DagBag

sys.path.append("dags")


@pytest.fixture(scope="function")
def dag_bag() -> DagBag:
    return DagBag(dag_folder="dags/", include_examples=False)
