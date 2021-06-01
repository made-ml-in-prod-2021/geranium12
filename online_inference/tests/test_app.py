#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from src.datamodel.request import InputDataModel


def test_main(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_predict(client, test_data):
    response = client.post(
        "/predict", data=json.dumps([sample.__dict__ for sample in test_data])
    )
    assert response.status_code == 200
    assert len(response.json()) == len(test_data)
    assert response.json()[0]["id"] == 0
    assert response.json()[0]["target"] in [0, 1]


def test_wrong_type(client):
    sample = InputDataModel()
    sample.cp = 'meow'
    response = client.post("/predict", data=json.dumps([sample.__dict__]))
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"


def test_wrong_value(client):
    sample = InputDataModel()
    sample.chol = 700
    response = client.post("/predict", data=json.dumps([sample.__dict__]))
    assert response.status_code == 400
    assert (
            response.json()["detail"]
            == "chol should be less than or equal to 600 and greater than or equal to 100"
    )
