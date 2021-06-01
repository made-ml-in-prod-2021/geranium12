#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pydantic import BaseModel


class OutputDataModel(BaseModel):
    id: int
    target: int
