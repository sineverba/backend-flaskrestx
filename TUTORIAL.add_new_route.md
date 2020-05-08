Small tutorial - Add new route
==============================

### How to add some other route (e.g. "auth/login")

1. Create the test `tests/v1/functional/auth/test_auth`

2. Run test and assure it fails

```bash
$ docker-compose up -d
$ docker-compose exec app python -m pytest "project/tests"
```

3. Import the namespace in `__init__.py`

```bash
from project.api.v1.auth.auth import auth_namespace
[...]
api.add_namespace(auth_namespace, path="/api/v1/auth");
```

4. Add a folder and a file `api/v1/auth/auth.py`

