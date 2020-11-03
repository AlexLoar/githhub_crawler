FROM python:3.8.1-slim-buster

ENV WORKDIR=/code
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR $WORKDIR

RUN pip install --upgrade pip
COPY requirements.txt $WORKDIR/
RUN pip install -r requirements.txt
