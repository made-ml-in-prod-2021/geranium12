from ml_project.data import read_data


def test_read_data(dataset_path: str, target_column: str):
    data = read_data(dataset_path)
    assert len(data) > 20
    assert target_column in data.keys()
