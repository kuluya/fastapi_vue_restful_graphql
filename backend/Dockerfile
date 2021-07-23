FROM python:3.9-alpine

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN set -eux \
 && apk add --no-cache build-base \
 && apk add --no-cache postgresql-libs \
 && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
 && pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir --trusted-host pypi.python.org -r /backend/requirements.txt \
 && apk del build-base \
 && rm -rf /root/.cache/pip

COPY . /backend
