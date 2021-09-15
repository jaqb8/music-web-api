FROM python:3.7-alpine
MAINTAINER Music App Team

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-dep \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D user
USER user