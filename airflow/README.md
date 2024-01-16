# Airflow Tutorial

setup airflow using docker compose 

* step 1.

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker compose up airflow-init
```

last command will take some time to pull all the docker images and create databases. after completion, run below command

```bash
docker compose up -d
```
> above will start the docker containers and services , you can visualize the airflow home page using below url

```
http://localhost:8080/home
username: airflow
pw:airflow
```

* step 2.

create simple bashoperator tasks for intial testing , add three simple bash echo commands and add task dependancy.

