FROM ubuntu:16.04

RUN apt update && apt upgrade -y
RUN apt install -y python3-pip python-virtualenv nodejs npm coffeescript
RUN npm install -g grunt
COPY . /app/
WORKDIR /app/static
RUN npm install
WORKDIR /app
RUN virtualenv /venv -p python3
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install -r requirements.txt
