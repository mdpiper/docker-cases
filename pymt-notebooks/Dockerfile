FROM condaforge/miniforge3

RUN conda install notebook pymt git -c conda-forge

WORKDIR /opt
RUN git clone https://github.com/csdms/pymt
WORKDIR /opt/pymt/notebooks

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.file_to_run='welcome.ipynb'", "--NotebookApp.token='csdms'"]
