FROM python:3.10-slim-buster
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install gunicorn
RUN mkdir /var/log/mailman
RUN apt-get update -y  && apt-get install -y default-libmysqlclient-dev python-dev && apt install build-essential -y
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENTRYPOINT sh entrypoint.sh
