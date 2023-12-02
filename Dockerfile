FROM python:3.11.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .
COPY /app/.env /app/app/.env

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

RUN apt-get update
RUN apt-get install -y nano

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
