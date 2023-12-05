# Build software for JOSS #6079.
# 
# Use:
#   docker build --tag joss-6079 [--label setup-1] .
#   docker run joss-6079
#   docker run -it joss-6079 bash

FROM ubuntu:22.04

RUN apt update
RUN apt install -y build-essential gfortran git autoconf gdal-bin libgdal-dev netcdf-bin libnetcdff-dev curl

# Install Julia through Juliaup: https://github.com/JuliaLang/juliaup
RUN curl -fsSL https://install.julialang.org | sh -s -- -y
RUN . /root/.bashrc

WORKDIR /opt
RUN git clone https://github.com/jakelangham/kestrel/
WORKDIR /opt/kestrel

RUN autoreconf -fi
RUN ./configure
RUN make

CMD [ "./src/kestrel" ]
