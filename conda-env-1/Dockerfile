FROM conda/miniconda3-centos7

WORKDIR /opt
COPY environment.yml .
COPY run.py .

RUN conda env create --file environment.yml

# See https://pythonspeed.com/articles/activate-conda-dockerfile/
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
ENTRYPOINT ["conda", "run", "-n", "myenv", "python", "run.py"]
