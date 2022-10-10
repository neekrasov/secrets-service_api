FROM python:3.11-rc-bullseye

WORKDIR /usr/src/secrets_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip
RUN pip install poetry 
RUN poetry config virtualenvs.create false
RUN poetry install --without dev --no-root

COPY . ./

CMD python3.11 main.py