from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.dates import days_ago

from dags.utils import default_args, DATA_RAW_PATH, MODEL_PATH, PREDICTIONS_PATH, VOLUMES_DIR

with DAG(
        "3_predict_pipeline",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(10),
) as dag:
    check_data = ExternalTaskSensor(
        task_id="check-data",
        external_dag_id="1_download_data",
        external_task_id="download_data",
        check_existence=True,
        timeout=100,
    )

    predict_model = DockerOperator(
        image="airflow-predict-model",
        command=f"-d {DATA_RAW_PATH} -m {MODEL_PATH} -p {PREDICTIONS_PATH}",
        network_mode="bridge",
        task_id="predict_model",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[VOLUMES_DIR],
    )

    check_data >> predict_model
