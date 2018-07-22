# MAINTANER Fernando Lobato "felobato@microsoft.com"

FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev \
    libpq-dev libjpeg-dev libxml2-dev libxslt-dev libfreetype6-dev libffi-dev

ENV LISTEN_PORT=8000

EXPOSE 5000

COPY ./app/requirements.txt ./app/requirements.txt 

RUN pip3 install -r app/requirements.txt

WORKDIR /workdir

COPY . /workdir

ENTRYPOINT [ "python3" ]

CMD [ "app/main.py" ]