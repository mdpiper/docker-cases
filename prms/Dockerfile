# PRMS components demo image
FROM conda/miniconda3

WORKDIR /opt
COPY prms-python.yaml .

RUN conda env create --file prms-python.yaml
RUN echo "source activate pyprms" > ~/.bashrc
ENV PATH /usr/local/envs/pyprms/bin:$PATH

ENTRYPOINT ["jupyter", "console"]

# docker build --tag prms-demo .
# docker run -i -t prms-demo
