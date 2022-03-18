FROM python:3.9-slim

ENV PYTHONPATH='/app'
WORKDIR /app

RUN apt-get update && apt-get -y install gcc

RUN pip install pip poetry -U --no-cache

COPY . .

RUN poetry config virtualenvs.create false && poetry install --no-interaction && pip uninstall --yes poetry

EXPOSE 8000

CMD python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload