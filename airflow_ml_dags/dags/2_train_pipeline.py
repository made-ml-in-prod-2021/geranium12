from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.dates import days_ago

from dags.utils import default_args, DATA_RAW_PATH, DATA_SPLIT_PATH, VOLUMES_DIR, DATA_PROCESSED_PATH, \
    MODEL_PATH

with DAG(
        "2_train_pipeline",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(10),
) as dag:
    check_data = ExternalTaskSensor(
        task_id="check_data",
        external_dag_id="1_download_data",
        external_task_id="download_data",
        check_existence=True,
        timeout=100,
    )

    split_data = DockerOperator(
        image="airflow-split-data",
        command=f"-l {DATA_RAW_PATH} -s {DATA_SPLIT_PATH}",
        network_mode="bridge",
        task_id="split_data",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[VOLUMES_DIR],
    )

    fit_transformer = DockerOperator(
        image="airflow-fit-transformer",
        command=f"-l {DATA_SPLIT_PATH} -s {DATA_PROCESSED_PATH} -m {MODEL_PATH}",
        network_mode="bridge",
        task_id="fit_transformer",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[VOLUMES_DIR],
    )

    fit_model = DockerOperator(
        image="airflow-fit-model",
        command=f"-d {DATA_PROCESSED_PATH} -m {MODEL_PATH}",
        network_mode="bridge",
        task_id="fit_model",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[VOLUMES_DIR],
    )

    validate_model = DockerOperator(
        image="airflow-validate-model",
        command=f"-d {DATA_PROCESSED_PATH} -m {MODEL_PATH}",
        network_mode="bridge",
        task_id="validate_model",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[VOLUMES_DIR],
    )

    check_data >> split_data >> fit_transformer >> fit_model >> validate_model
