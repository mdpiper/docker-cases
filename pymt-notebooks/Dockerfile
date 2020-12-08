FROM condaforge/miniforge3

WORKDIR /opt
COPY requirements.txt .

RUN conda install -c conda-forge --file=requirements.txt

RUN git clone https://github.com/csdms/pymt
WORKDIR /opt/pymt/notebooks

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.file_to_run=welcome.ipynb", "--NotebookApp.token=csdms"]
