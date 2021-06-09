import os
from datetime import timedelta

default_args = {
    "owner": "Hanna Herasimchyk",
    "email": ["airflow@example.com"],
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

LOCAL_DATA_DIR = os.environ["LOCAL_DATA_DIR"]
VOLUMES_DIR = f"{LOCAL_DATA_DIR}:/data"

DATA_RAW_PATH = "/data/raw/{{ ds }}"
DATA_SPLIT_PATH = "/data/split/{{ ds }}"
DATA_PROCESSED_PATH = "/data/processed/{{ ds }}"

MODEL_PATH = "/data/models/{{ ds }}"
PREDICTIONS_PATH = "/data/predictions/{{ ds }}"
