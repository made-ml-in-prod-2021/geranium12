Airflow 
==============================

### Usage:
1. You must define a local variable _%LOCAL_DATA_PATH%_ with path for data (models, transformers, dataset). 
2. Then set airflow database.
```
docker-compose up airflow-init
```
3. After that, you should run the airflow app.
```
docker-compose up --build
```
4. Happily go to http://localhost:8080/.

Moreover, you can provide _email_ and _password_ for getting an email alert if dag goes off.
```
set GMAIL_USERNAME=<your_user_name>
set GMAIL_PASSWORD=<your_password>
```

5. However, if you want to stop the airflow app, you should press Ctrl + C and enter the following code
```
docker-compose down
```

### Test:
Firstly, start the airflow app. 
Secondly, go into the _airflow scheduler docker container_.
```
docker exec -it AIRFLOW_SCHEDULER_CONTAINER_ID bash
pytest -v .
```
