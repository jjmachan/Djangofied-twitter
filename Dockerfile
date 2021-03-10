FROM python:3.8.5-slim

COPY ./requirements.txt /deploy/app/

RUN pip install -r /deploy/app/requirements.txt

WORKDIR /deploy/app
COPY . /deploy/app

CMD python3 manage.py runserver 0.0.0.0:8000
