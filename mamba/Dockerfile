FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install wget -y

WORKDIR /usr/local
RUN wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba

RUN micromamba shell init -s bash -p ~/micromamba
RUN . ~/.bashrc
# SHELL ["source", "~/.bashrc"]
# ENV PATH /root/micromamba/condabin:$PATH
ENV PATH /root/micromamba/bin:$PATH

RUN micromamba activate
# SHELL [ "micromamba", "activate" ]
RUN micromamba install -y python=3.8 flask
# SHELL [ "micromamba", "install", "-y", "python=3.8", "flask" ]

# RUN echo "source activate myenv" > ~/.bashrc
# ENV PATH /usr/local/envs/myenv/bin:$PATH

# ENTRYPOINT ["python", "run.py"]

# docker build --tag mamba .
# docker run -it mamba bash
