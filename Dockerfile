FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install gettext -y
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
RUN pip3 install pyOpenSSL --upgrade

COPY . /app

EXPOSE 8080