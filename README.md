
Production-ready project for heart disease classification
==============================

### Installation:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage:
```
python -m models.train_pipeline
python -m models.predict_pipeline
```

### Test:
```
pytest tests/
```

### Report creation:
```
python -m ml_project.visualization.eda
```

### Dataset:
Dataset [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci) is used for the project. 
Data must be in .csv format in data/raw directory.

### Hydra Configuration:
Configs are in configs/ directory.
All Hydra configs must be described as dataclasses in ml_project/config/. 


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── ml_project                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    |   |   └── transformer.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_pipeline.py
    │   │   └── train_pipeline.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── eda.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
