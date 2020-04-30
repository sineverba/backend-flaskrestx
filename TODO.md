+ Renable all calls to db into project
+ Add `sqlite` as database for testing
+ Move from `project` to `app`
+ Add `ping` under folder
+ Move from `migrate(app)` to `migrate.init_app(app)` in `__init__.py`
+ Remove "Secret key" from `config.py`
+ Add Version in PING dinamic from tag
+ Move `ping.py` under `controller`
+ Change Dockerfile.postgres to use the createsql to echo into the initdb-d