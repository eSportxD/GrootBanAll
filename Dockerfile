FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git python3-pip -y
RUN pip3 install -U pip
WORKDIR /banall/
COPY . /banall/
pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD python3 banall.py
