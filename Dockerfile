FROM python:3.12.5-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
