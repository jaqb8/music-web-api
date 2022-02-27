FROM python:3.8-alpine
ENV PYTHONBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++

WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .