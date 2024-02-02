FROM python:3.11.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y nano \
    netcat-traditional \
    binutils \
    libproj-dev \
    gdal-bin

RUN addgroup --system automatico-api && \
    adduser --system --group automatico-api

ENV APP_HOME=/home/automatico-api/app
RUN mkdir -p $APP_HOME/static && \
    mkdir -p $APP_HOME/media

WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install psycopg2-binary \
    gunicorn==21.2.0

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

COPY . .

RUN chown -R automatico-api:automatico-api $APP_HOME
USER automatico-api

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
