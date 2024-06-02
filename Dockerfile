FROM python:3.11

WORKDIR /app/islywebsite

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    default-mysql-client \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/islywebsite/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uwsgi

COPY . /app/islywebsite/

ENV DJANGO_SETTINGS_MODULE=islyweb.settings
ENV PYTHONUNBUFFERED=1

RUN python manage.py collectstatic --noinput \
    && chown -R 1000:1000 /app/islywebsite/staticfiles