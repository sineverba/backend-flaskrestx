#!/bin/sh

docker exec app python -m pytest "project/tests";
docker exec app black project;
docker exec app flake8 project;
docker exec app isort project/**/*.py;