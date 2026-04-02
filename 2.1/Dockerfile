FROM quay.io/jupyter/minimal-notebook:2026-04-02

ARG JUPYTERHUB_VERSION=5.4.4

RUN pip3 install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION

RUN pip3 install --no-cache -r Intrusion-detection/requirements.txt