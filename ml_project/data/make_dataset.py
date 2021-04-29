#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data
