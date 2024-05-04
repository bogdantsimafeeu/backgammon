FROM python:3.12-slim

RUN mkdir /backgammon

WORKDIR /backgammon

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

