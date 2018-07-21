# MAINTANER Fernando Lobato "felobato@microsoft.com"

FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev \
    libpq-dev libjpeg-dev libxml2-dev libxslt-dev libfreetype6-dev libffi-dev

EXPOSE 5000

COPY ./app ./app

WORKDIR ./app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]