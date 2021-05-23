#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import HTTPException
from pydantic import BaseModel, validator


class InputDataModel(BaseModel):
    id: int = 0
    age: int = 50
    sex: int = 0
    cp: int = 2
    trestbps: int = 150
    chol: int = 200
    fbs: int = 0
    restecg: int = 1
    thalach: int = 150
    exang: int = 1
    oldpeak: float = 0.786
    slope: int = 2
    ca: int = 0
    thal: int = 2

    @validator("id")
    def validate_id(cls, value):
        if value < 0:
            raise HTTPException(
                status_code=400, detail="id should be greater tha or equal to 0"
            )
        return value

    @validator("age")
    def validate_age(cls, value):
        if value < 0 or value > 130:
            raise HTTPException(
                status_code=400,
                detail="age should be less than or equal to 130 and greater"
                       " than or equal to 0",
            )
        return value

    @validator("sex")
    def validate_sex(cls, value):
        if value not in [0, 1]:
            raise HTTPException(status_code=400, detail="sex should be equal to 0 or 1")
        return value

    @validator("cp")
    def validate_cp(cls, value):
        if value not in [0, 1, 2, 3]:
            raise HTTPException(
                status_code=400,
                detail="cp should be equal to 0, or 1, or 2, or 3",
            )
        return value

    @validator("trestbps")
    def validate_trestbps(cls, value):
        if value < 50 or value > 250:
            raise HTTPException(
                status_code=400,
                detail="trestbps should be greater than or equal to 50 and less"
                       " than or equal to 250",
            )
        return value

    @validator("chol")
    def validate_chol(cls, value):
        if value < 100 or value > 600:
            raise HTTPException(
                status_code=400,
                detail="chol should be less than or equal to 600 and greater"
                       " than or equal to 100",
            )
        return value

    @validator("fbs")
    def validate_fbs(cls, value):
        if value not in [0, 1]:
            raise HTTPException(
                status_code=400,
                detail="fbs should be equal to 0 or 1",
            )
        return value

    @validator("restecg")
    def validate_restecg(cls, value):
        if value not in [0, 1, 2]:
            raise HTTPException(
                status_code=400,
                detail="restecg should be equal to 0, or 1, or 2",
            )
        return value

    @validator("thalach")
    def validate_thalach(cls, value):
        if value < 50 or value > 250:
            raise HTTPException(
                status_code=400,
                detail="thalach should be less than or equal to 250 and greater"
                       " than or equal to 50",
            )
        return value

    @validator("exang")
    def validate_exang(cls, value):
        if value not in [0, 1]:
            raise HTTPException(
                status_code=400,
                detail="exang should be equal to 0 or 1",
            )
        return value

    @validator("oldpeak")
    def validate_oldpeak(cls, value):
        if value < 0 or value > 10:
            raise HTTPException(
                status_code=400,
                detail="oldpeak should be less than or equal to 10 and greater"
                       " than or equal to 0",
            )
        return value

    @validator("slope")
    def validate_slope(cls, value):
        if value not in [0, 1, 2]:
            raise HTTPException(
                status_code=400,
                detail="slope should be equal to 0, or 1, or 2",
            )
        return value

    @validator("ca")
    def validate_ca(cls, value):
        if value not in [0, 1, 2, 3, 4]:
            raise HTTPException(
                status_code=400,
                detail="ca should be equal to 0, or 1, or 2, or 3, or 4",
            )
        return value

    @validator("thal")
    def validate_thal(cls, value):
        if value not in [0, 1, 2, 3]:
            raise HTTPException(
                status_code=400,
                detail="thal should be equal to 0, or 1, or 2, or 3",
            )
        return value
