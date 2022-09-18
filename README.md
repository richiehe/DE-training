## Python Env
```shell
pyenv virtualenv 3.10.4 training
pyenv activate training
```

## Setup Database
```shell
docker-compose up
```

### DB migration
```shell
bash ./scripts/db-migration.sh
```

## Setup Airflow
```shell
bash ./scripts/airflow-bootstrap.sh
```