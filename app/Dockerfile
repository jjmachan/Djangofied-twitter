FROM python:3.8.5-alpine

WORKDIR /deploy/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /deploy/app/
RUN pip install -r /deploy/app/requirements.txt

COPY . /deploy/app
