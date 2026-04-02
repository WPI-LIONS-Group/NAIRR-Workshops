FROM quay.io/jupyter/minimal-notebook:python-3.11

ARG JUPYTERHUB_VERSION=5.4.4

WORKDIR /src

COPY . .

RUN pip3 install --no-cache -r ./Intrusion-detection/requirements.txt

RUN pip3 install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION

ENV HOME=/home/jovyan
WORKDIR $HOME