#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from fastapi.testclient import TestClient

from app import app
from src.datamodel.request import InputDataModel


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def test_data():
    data_0 = {
        "id": 0,
        "age": 36,
        "sex": 1,
        "cp": 1,
        "trestbps": 130,
        "chol": 180,
        "fbs": 1,
        "restecg": 0,
        "thalach": 129,
        "exang": 0,
        "oldpeak": 0.98,
        "slope": 1,
        "ca": 1,
        "thal": 2,
    }
    data_1 = {
        "id": 1,
        "age": 65,
        "sex": 0,
        "cp": 1,
        "trestbps": 165,
        "chol": 198,
        "fbs": 0,
        "restecg": 1,
        "thalach": 135,
        "exang": 1,
        "oldpeak": 0.46,
        "slope": 1,
        "ca": 0,
        "thal": 1,
    }
    data_2 = {
        "id": 2,
        "age": 72,
        "sex": 1,
        "cp": 1,
        "trestbps": 164,
        "chol": 179,
        "fbs": 1,
        "restecg": 0,
        "thalach": 183,
        "exang": 1,
        "oldpeak": 1.05,
        "slope": 2,
        "ca": 0,
        "thal": 1,
    }
    data = [
        InputDataModel(**data_0),
        InputDataModel(**data_1),
        InputDataModel(**data_2),
    ]
    return data
