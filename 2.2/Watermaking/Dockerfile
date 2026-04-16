FROM quay.io/jupyter/pytorch-notebook:cuda12-latest

ARG JUPYTERHUB_VERSION=5.4.4

COPY ./requirements.txt .

RUN pip3 install --no-cache -r requirements.txt

# RUN pip3 uninstall torch torchvision torchaudio

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

RUN pip3 install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION

RUN pip3 install --no-cache \
    nbgitpuller