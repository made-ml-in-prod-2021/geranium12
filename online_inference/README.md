
Online inference for heart disease classification project
==============================

### Docker:
```
docker pull hherasimchyk/online_inference:v1 (or docker build -t hherasimchyk/online_inference:v1 .)
docker run -it -p 8000:8000 hherasimchyk/online_inference:v1
```

### Make a request:
```
python src/make_request.py
```

### Test:
```
python -m pytest tests/
```

### Docker image size optimization:
Python:3.7.10-slim-stretch is used to reduce docker image size from 1.5Gb to 600.2Mb (compressed 276.57Mb).

### Test Data:
Dataset [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci) is used for the project. 
Test data must be in .csv format in data/raw directory.


### Project Organization:
------------

    ├── README.md             <- The top-level README for developers using this project.
    ├── data
    │   └── raw               <- The original, immutable data dump.
    |
    ├── dist                  <- Libraries (e.g. ml_project) for the online inference.
    |
    ├── models                <- Dumped pipelines (model + transformer) for making predictions.
    |
    ├── src                   <- Source code for use in this project.
    │   ├── datamodel         <- Scripts of input and output data models for fastapi app.
    │   │
    |   └── make_request.py   <- Script to make a request to get predictions.
    |
    ├── tests                 <- Scripts for testing the whole fastapi app.
    │   ├── conftest.py      
    |   └── test_app.py       
    |
    ├── Dockerfile            <- Docker file which contains all the commands to create an image.
    |
    ├── __init__.py           <- Makes app a Python module.
    |
    ├── app.py                <- Main file with the fastapi app.
    |
    ├── requirements.txt      <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`.
    │
    └── setup.py              <- makes project pip installable (pip install -e .) so src can be imported.
   
