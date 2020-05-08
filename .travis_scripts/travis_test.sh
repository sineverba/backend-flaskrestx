#!/bin/sh

docker exec app python -m pytest "project/tests";
docker exec app /home/root/.local/bin/black project;
docker exec app /home/root/.local/bin/flake8 project;
docker exec app /home/root/.local/bin/isort project/**/*.py;