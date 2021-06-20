from airflow.models import DagBag


def test_download_data_dag(dag_bag: DagBag):
    assert "1_download_data" in dag_bag.dags
    assert len(dag_bag.dags["1_download_data"].tasks) == 1
    structure = {
        "download_data": []
    }
    dag = dag_bag.dags["1_generate_data"]
    for name, task in dag.task_dict.items():
        assert set(structure[name]) == task.downstream_task_ids


def test_train_pipeline_dag(dag_bag):
    assert "2_train_pipeline" in dag_bag.dags
    assert len(dag_bag.dags["2_train_pipeline"].tasks) == 5
    structure = {
        "check_data": ["split_data"],
        "split_data": ["fit_transformer"],
        "fit_transformer": ["fit_model"],
        "fit_model": ["validate_model"],
        "validate_model": [],
    }
    dag = dag_bag.dags["2_train_pipeline"]
    for name, task in dag.task_dict.items():
        assert set(structure[name]) == task.downstream_task_ids


def test_predict_pipeline_dag(dag_bag):
    assert "3_predict_pipeline" in dag_bag.dags
    assert len(dag_bag.dags["3_predict_pipeline"].tasks) == 2
    structure = {
        "check_data": ["predict_model"],
        "predict_model": [],
    }
    dag = dag_bag.dags["3_predict_pipeline"]
    for name, task in dag.task_dict.items():
        assert set(structure[name]) == task.downstream_task_ids


def test_dag_bag_import(dag_bag):
    assert dag_bag.dags is not None
    assert dag_bag.import_errors == {}
