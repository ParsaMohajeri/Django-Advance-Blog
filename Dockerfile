FROM python:3.8-slim-buster


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app

COPY . /app
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt




CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
