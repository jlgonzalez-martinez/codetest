FROM python:3.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./ /app

WORKDIR /app

RUN apt-get update && apt-get install \
    build-essential \
    curl \
    pkg-config -y \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apt/lists

EXPOSE 9090
CMD export PYTHONPATH=${PYTHONPATH}:/app && python app/main.py -c app/config.yml
