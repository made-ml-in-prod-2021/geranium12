#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import os

import pandas as pd
import requests

HOST = os.environ.get("HOST", default="0.0.0.0")
PORT = os.environ.get("PORT", default="8000")
DATA_PATH = os.environ.get("DATA_PATH", default="data/raw/test.csv")

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    df["id"] = range(len(df))
    data = df.to_dict(orient="records")
    response = requests.post(
        url=f"http://{HOST}:{PORT}/predict",
        json=json.dumps(data)
    )
    logger.info(f"Status code:\t{response.status_code}")
    if response.status_code == 200:
        logger.info(f"Request:\t{df.head()}")
        logger.info(f"Response:\t{response.json()[:5]}")
    else:
        logger.info(f"Error:\t{response.text}")
