#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import pickle
import time
from typing import List, Optional

import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
from ml_project.features import MinMaxTransformer
from ml_project.models.train_pipeline import predict_model
from sklearn.svm import SVC

from src.datamodel.request import InputDataModel
from src.datamodel.response import OutputDataModel

transformer: Optional[MinMaxTransformer] = None
model: Optional[SVC] = None

app = FastAPI()
logger = logging.getLogger(__name__)


@app.on_event("startup")
def load_pipeline():
    model_path = os.getenv("PATH_TO_MODEL", default="models/model.pkl")
    try:
        logger.info("Loading pipeline...")
        with open(model_path, "rb") as f:
            pipeline = pickle.load(f)
    except FileNotFoundError as err:
        logger.error(err)
        return
    global transformer, model
    transformer = pipeline["transformer"]
    model = pipeline["model"]
    logger.info("Getting model and transformer...")


@app.get("/")
def main():
    return "Hey! It's an entry point :)"


@app.get("/health")
def health() -> bool:
    logger.info("Checking health status...")
    time.sleep(120)
    raise Exception
    return not (model is None or transformer is None)


@app.post("/predict", response_model=List[OutputDataModel])
def predict(request: List[InputDataModel]):
    if not health():
        logger.error("Model is not available")
        raise HTTPException(status_code=500, detail="Model is not available")
    logger.info("Starting prediction...")
    df = pd.DataFrame(sample.__dict__ for sample in request)
    logger.info(f"Input data:\t{df.head()}")
    transformed_data = transformer.transform(df.drop("id", axis=1))
    predictions = predict_model(model, transformed_data)
    logger.info(f"Predictions:\t{predictions.head()}")
    response = []
    for i in range(len(predictions)):
        response.append(OutputDataModel(id=df["id"][i], target=predictions[0][i]))
    return response


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
