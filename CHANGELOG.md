# Next version

### Refactor
+ Get API VERSION from env

## 0.5.0

### Add
+ Add `auth/login` route with fake output
+ Add `nginx` as reverse proxy for gunicorn

### Refactor
+ Move `crud.py` under `api/v1/accounts`
+ Move `accounts` under `api/v1/accounts`
+ Move tests under `v1` folder

## 0.4.0

### Refactor
+ Refactor custom_account view (Change fields to render)
+ Add accounts into envelope

## 0.3.0
+ Small refactor on ping
+ Add setup.cfg for flake
+ Crypt passwords
+ Add other tests

## 0.2.1
+ Fix `deleted_at` field not null at first create

## 0.2.0

### Add
+ Add Flake8, Isort and Black
+ Add Postgres Database
+ Add tests for ping
+ Reenable all calls to DB
+ Add Bcrypt
+ Add `accounts` models and table

## 0.1.0
+ First version