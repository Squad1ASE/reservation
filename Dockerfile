FROM python:3.8-alpine

ADD . /reservation
WORKDIR /reservation

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
RUN python setup.py develop

EXPOSE 6000
