FROM python:3.8.10-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc
RUN pip install --upgrade pip setuptools wheel

RUN apk add musl-dev

RUN pip install -r /requirements.txt --default-timeout=100

RUN pip install tzdata

RUN apk add --no-cache g++


RUN mkdir /onlineJudge
COPY . /onlineJudge
WORKDIR /onlineJudge
