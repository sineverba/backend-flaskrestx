Small tutorial - Base
=====================

This is a small tutorial, how I coded this.

1. Setup dependencies

``` bash
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget
$ sudo apt install python3.8 python3-pip python3-setuptools python3.8-venv -y
```

2. Create a new virtual environment

`$ python3.8 -m venv env`

3. Activate the virtual environment

`$ source env/bin/activate`

4. Setup some base requirements

``` bash
(env) $ pip install flask
(env) $ pip install flask-restx
```

5. Freeze the requirements

`(env) $ pip freeze > requirements.txt`

6. Split the requirements for future setup of develop requirements

`(env) $ touch requirements-dev.txt`

7. Create the main project folder

`(env) $ mkdir project`

8. Add the main configuration to the project folder (`config.py` file)

9. Set in your preferred continuous integration a very strong environment variable as `SECRET_KEY`. Generate as follow

``` bash
(env) $ python3.8
>>> import os
>>> import codecs
>>> print(codecs.encode(os.urandom(32), 'hex').decode())
794ac7b858bf55565275fcb87a9d9b86e1cfb7b658654438bd415c1463ca331f
```

10. Add the main file `__init__.py` into `project` folder. It uses the env var `APP_SETTINGS`.

> APP_SETTINGS is a environment variables with one of following values:
  - project.config.ProductionConfig
  - project.config.DevelopmentConfig
  - project.config.TestingConfig

> Got from Dockerfile / docker-compose

11. Add the main `manage.py` file (db commented)

12. Add the `api` folder for next routes, with `__init__.py` and `ping.py` file

13. Export the env vars and launch `python manage.py run`. Visit `http://localhost:5000/api/v1/ping`.

14. Add `pytest` and the `tests` directory, with `conftest.py`. Assure that can start with `python -m pytest "project/tests"`

15. Add a unit test for configuration (`tests/unit/test_config.py`) and run it with `python -m pytest "project/tests"`

16. Add the coverage (pytest-cov and `.coveragerc` file) and run it with `python -m pytest "project/tests" --cov="project"`

17. Add the `CODECOV_TOKEN` env var to your Continuous Integration system

18. Dockerize the app

19. Add the Docker for auto deploy (`docker/Dockerfile.prod`)

``` bash
$ heroku container:login
$ docker build -f ./docker/Dockerfile.prod -t registry.heroku.com/backend-flaskrestx/web .
$ docker push registry.heroku.com/backend-flaskrestx/web:latest
$ heroku container:release web --app backend-flaskrestx
$ heroku run sh
$ export FLASK_APP=project/__init__.py
$ flask shell
>>> app.config["SECRET_KEY"]
```

20. Add the HEROKU_API_KEY in Continuous Integration settings

``` bash
$ heroku authorizations:create
```

21. Add the Database (Postgres)

    1. Note in `project/config.py` 2 database URIs (one for test, one for dev and production)
    2. Create the `db/create.sql` instructions and the `Dockerfile.postgres` Dockerfile
    3. Update the `docker-compose` file
    4. Add an entrypoint for user, to wait for postgres
    5. Rebuild the images `docker-compose up --build`

22. Reneable all call to DB into `conftest.py` and `manage.py`

23. Install Bcrypt

    1. Update `project/config.py` with BCRYPT and TOKEN datas
    2. Init app with bcrypt in `project/__init__.py`
    3. Update Dockerfile with `libffi-dev`

24. Add the accounts model (accounts, crud and models)

25. Add the route to api/init.py

26. Migrate the database

``` bash
$ docker-compose exec app python manage.py db init
$ docker-compose exec app python manage.py db migrate -m "Initial migration"
```

27. Apply the migration

``` bash
$ docker-compose exec app python manage.py db migrate upgrade
```

28. Add a Postres Database to Heroku