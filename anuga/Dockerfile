FROM condaforge/miniforge3

WORKDIR /opt
COPY requirements.txt .

RUN conda install -c conda-forge --file=requirements.txt
RUN pip install triangle Pmw

RUN git clone https://github.com/GeoscienceAustralia/anuga_core.git
WORKDIR /opt/anuga_core
RUN git checkout anuga_py3

# RUN python setup.py install
CMD [ "python", "setup.py", "install" ]

# docker build --tag anuga .
# docker run -it --rm anuga
