FROM conda/miniconda3-centos7

WORKDIR /opt
COPY environment.yml .
COPY run.py .

RUN conda env create --file environment.yml

# https://medium.com/@chadlagore/conda-environments-with-docker-82cdc9d25754
RUN echo "source activate myenv" > ~/.bashrc
ENV PATH /usr/local/envs/myenv/bin:$PATH
ENTRYPOINT ["python", "run.py"]
