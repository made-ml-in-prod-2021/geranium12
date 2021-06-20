from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

from dags.utils import default_args, DATA_RAW_PATH, VOLUMES_DIR

with DAG(
        "1_download_data",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(10),
) as dag:
    download_data = DockerOperator(
        image="airflow-download-data",
        command=f"-s {DATA_RAW_PATH}",
        network_mode="bridge",
        task_id="download_data",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[VOLUMES_DIR],
    )

    download_data
