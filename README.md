Backend Flask RESTX: Python backend with Flask RESTX + JWT Token
================================================================

Do you like it or do you use it? **Star it!**

| CI/CD  | Status                                                                                                                                          |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Travis | [![Build Status](https://api.travis-ci.com/sineverba/backend-flaskrestx.svg?branch=master)](https://travis-ci.com/sineverba/backend-flaskrestx) |


## Run in development (Docker mode)

__TODO__

## Run in development (Local installation)

1. Create a new virtual environment

`$ python3.8 -m venv env`

2. Activate the virtual environment

`$ source env/bin/activate`

3. Setup the requirements (requirements-dev.txt will setup also develop tools)

`(env) $ pip install -r requirements-dev.txt`

4. Export the environment variables

``` bash
(env) $ export SECRET_KEY=ThisIsMySuperLongAndSuperSecretKey
(env) $ export DATABASE_TEST_URL=prefix://username:password@host:port/database

```

----------------------------------------------------------------------------------------------------------------------


#### Small tutorial

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

9. Set in Continuous Integration a very strong environment variable as `SECRET_KEY`. Generate as follow

``` bash
(env) $ python3.8
>>> import os
>>> import codecs
>>> print(codecs.encode(os.urandom(32), 'hex').decode())
794ac7b858bf55565275fcb87a9d9b86e1cfb7b658654438bd415c1463ca331f
```