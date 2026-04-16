FROM quay.io/jupyter/pytorch-notebook:cuda12-latest

ARG JUPYTERHUB_VERSION=5.4.4

COPY ./requirements.txt .

RUN pip3 install --no-cache -r requirements.txt

# RUN pip3 uninstall torch torchvision torchaudio

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# update the gpu driver
RUN apt-get update && apt-get install -y --no-install-recommends \
    nvidia-driver-535 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION

RUN pip3 install --no-cache \
    nbgitpuller