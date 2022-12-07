FROM ubuntu:18.04

RUN apt-get update && apt-get -y install sudo

RUN apt update -y
RUN apt install python3.6 -y
RUN apt install vim -y
RUN apt install net-tools -y
RUN apt install iputils-ping -y
RUN apt install python3-pip -y
# RUN apt-get install git

RUN apt update -y
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN apt update -y

ENV FLASK_APP ./src/app.py
ENV FLASK_ENV development
ENV FLASK_RUN_HOST 127.0.0.1

ENV LC_ALL en_US
RUN export LC_ALL
ENV PYTHONPATH="${PYTHONPATH}:/app"
WORKDIR /app
