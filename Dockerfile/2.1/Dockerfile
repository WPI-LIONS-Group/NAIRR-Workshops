FROM quay.io/jupyter/minimal-notebook:python-3.11

ARG JUPYTERHUB_VERSION=5.4.4

COPY ./Intrusion-detection/requirements.txt .

RUN pip3 install --no-cache -r requirements.txt

RUN pip3 install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION

RUN pip3 install --no-cache \
    nbgitpuller