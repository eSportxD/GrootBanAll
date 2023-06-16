FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git python3-pip -y
RUN pip3 install -U pip
WORKDIR /banall/
COPY . /banall/
RUN pip3 install -r requirements.txt
CMD python3 banall.py
