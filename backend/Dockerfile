FROM python:3.8.12-alpine3.15

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN gunicorn --worker-class eventlet -w 1 module:app -b 0.0.0.0:8000