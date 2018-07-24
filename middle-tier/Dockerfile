# MAINTANER Fernando Lobato "felobato@microsoft.com"

FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev \
    libpq-dev libjpeg-dev libxml2-dev libxslt-dev libfreetype6-dev libffi-dev

ENV LISTEN_PORT=8000

ENV API_KEY '380500510ecf4d9cbac74fdf566c9065'
ENV PRIVATE_KEY '389e3c80b20359988263bd3abd88a71eb5d964ddae1b3430cf4be61c7e17381f'
ENV CONTRACT_ADDRESS '0x313CaC645b2210b6591EEDd7a6D492521819CF1E'

EXPOSE 5000

COPY ./app/requirements.txt ./app/requirements.txt 

RUN pip3 install -r app/requirements.txt

WORKDIR /workdir

COPY . /workdir
COPY ./app/resources /workdir/resources

ENTRYPOINT [ "python3" ]

CMD [ "app/main.py" ]