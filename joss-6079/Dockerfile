# Build software for JOSS #6079.
# 
# Use:
#   docker build --tag joss-6079 .
#   docker run joss-6079

FROM ubuntu:22.04

RUN apt update
RUN apt install -y build-essential gfortran git autoconf gdal-bin libgdal-dev netcdf-bin libnetcdff-dev

# Install Julia: https://julialang.org/downloads/platform/#linux_and_freebsd

WORKDIR /opt
RUN git clone https://github.com/jakelangham/kestrel/
WORKDIR /opt/kestrel

RUN autoreconf -fi
RUN ./configure
RUN make

CMD [ "./src/kestrel" ]
