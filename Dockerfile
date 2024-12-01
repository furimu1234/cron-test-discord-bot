FROM python:3.13 as build

RUN apt-get -y update
RUN apt-get -y upgrade

RUN pip install uv

COPY . /root/same
WORKDIR /root/same
ENV UV_LINK_MODE="copy"

RUN uv sync
