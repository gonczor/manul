FROM ubuntu:16.04

RUN apt update && apt upgrade
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

COPY . /app/

EXPOSE 5000
CMD python3 /app/main.py 0.0.0.0:5000 &
