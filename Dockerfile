FROM python:3.11.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y nano && \
    apt-get install -y netcat-traditional

RUN addgroup --system prestamos-api && \
    adduser --system --group prestamos-api

ENV APP_HOME=/home/prestamos-api/app
RUN mkdir -p $APP_HOME/static && \
    mkdir -p $APP_HOME/media

WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install psycopg2-binary && \
    pip install gunicorn==21.2.0

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

COPY . .

RUN chown -R prestamos-api:prestamos-api $APP_HOME
USER prestamos-api

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
