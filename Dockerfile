# 베이스 이미지를 Python 3.11.9로 설정합니다.
FROM python:3.11.9-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 필요한 시스템 종속성을 설치합니다.
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python 종속성을 설치합니다.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스를 복사합니다.
COPY . /app/

# 환경 변수를 설정합니다.
ENV DJANGO_SETTINGS_MODULE=islyweb.settings
ENV PYTHONUNBUFFERED=1

# Django collectstatic 명령어를 실행합니다.
RUN python manage.py collectstatic --noinput

# 컨테이너가 외부와 통신할 포트를 지정합니다.
EXPOSE 80

# Gunicorn을 사용하여 Django 애플리케이션을 시작하는 명령어를 설정합니다.
CMD ["uwsgi", "--ini", "uwsgi.ini"]
