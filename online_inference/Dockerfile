FROM python:3.7.10-slim-stretch

COPY . .

RUN pip install -r /requirements.txt

RUN pip install dist/ml_project-0.1.0.tar.gz

WORKDIR .

ENV PATH_TO_MODEL="models/model.pkl"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]