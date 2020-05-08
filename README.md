Backend Flask RESTX: Python backend with Flask RESTX + JWT Token
================================================================

Do you like it or do you use it? **Star it!**

Project heavily inspired by [TestDriven course](https://testdriven.io)

Supports Python 3.6, 3.7 and 3.8

| CI/CD/Style/Compatibility | Status                                                                                                                                          |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Travis      | [![Build Status](https://api.travis-ci.com/sineverba/backend-flaskrestx.svg?branch=master)](https://travis-ci.com/sineverba/backend-flaskrestx)                         |
| Coverall    | [![Coverage Status](https://coveralls.io/repos/github/sineverba/backend-flaskrestx/badge.svg?branch=master)](https://coveralls.io/github/sineverba/backend-flaskrestx?branch=master) |
| Codecov     | [![codecov](https://codecov.io/gh/sineverba/backend-flaskrestx/branch/master/graph/badge.svg)](https://codecov.io/gh/sineverba/backend-flaskrestx)                         |
| Black       | [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)                                      |
| Python versions | [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)


## Run in development (Docker mode)

1. Build the docker image

`docker-compose build`

2. Start the docker-compose

`docker-compose up -d`

3. To run tests

```bash
$ docker-compose exec app python -m pytest "project/tests" --cov="project"
$ docker-compose exec app python -m pytest "project/tests" --cov="project" --cov-report="html"
$ docker-compose exec app black project --check
$ docker-compose exec app black project --diff
$ docker-compose exec app black project
$ docker-compose exec app isort project/**/*.py --check-only
$ docker-compose exec app isort project/**/*.py --diff
$ docker-compose exec app isort project/**/*.py
$ docker-compose exec app flake8 project
```

4. Inspect the Postgres database

```bash
$ docker-compose exec postgres psql -U username
```

## Run in development (Local installation)

1. Create a new virtual environment

`$ python3.8 -m venv env`

2. Activate the virtual environment

`$ source env/bin/activate`

3. Setup the requirements (requirements-dev.txt will setup also develop tools)

`(env) $ pip install -r requirements-dev.txt`

4. Export the environment variables

``` bash

(env) $ export FLASK_APP=project/__init__.py
(env) $ export FLASK_ENV=development
(env) $ export SECRET_KEY=ThisIsMySuperLongAndSuperSecretKey
(env) $ export DATABASE_TEST_URL=postgresql://username:password@host:5432/database
(env) $ export APP_SETTINGS=project.config.DevelopmentConfig

```