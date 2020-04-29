# pull official base image
FROM python:3.8.2-alpine

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY ThisIsMySuperLongAndSuperSecretKey

# add and install requirements
RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./requirements-dev.txt /usr/src/app/requirements-dev.txt

RUN pip install -r requirements-dev.txt

# add app
COPY . .

# run server
CMD python manage.py run -h 0.0.0.0