FROM ubuntu:18.04

ENV USER=mdpiper
RUN useradd -ms /bin/bash $USER
ENV HOMEDIR=/home/$USER

USER $USER
RUN echo $USER
WORKDIR /home/$USER

# docker build --tag user-example .
# docker run -it --rm user-example bash
