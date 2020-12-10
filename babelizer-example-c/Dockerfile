FROM condaforge/miniforge3

WORKDIR /opt
RUN git clone https://github.com/csdms/babelizer

# conda environments are wonky in Docker.
RUN conda env create --file babelizer/docs/source/environment.yml
RUN echo "source activate wrap" >> ~/.bashrc
ENV CONDA_PREFIX=/opt/conda/envs/wrap
ENV PATH ${CONDA_PREFIX}/bin:$PATH

RUN git clone https://github.com/csdms/bmi-example-c
WORKDIR /opt/bmi-example-c/_build
RUN cmake .. -DCMAKE_INSTALL_PREFIX=${CONDA_PREFIX} && make install

WORKDIR /opt
RUN babelize init babelizer/docs/source/babel_heatc.toml .

WORKDIR /opt/pymt_heatc 
RUN conda install -c conda-forge \
    --file=requirements-build.txt \
    --file=requirements-testing.txt \
    --file=requirements-library.txt \
    --file=requirements.txt

# This is a result of conda environments not working correctly in Docker.
ENV SYSROOT=${CONDA_PREFIX}/x86_64-conda-linux-gnu/sysroot
RUN mkdir -p /usr/lib64
RUN ln -s ${SYSROOT}/lib64/libpthread.so.0 /lib64/libpthread.so.0
RUN ln -s ${SYSROOT}/usr/lib64/libpthread_nonshared.a /usr/lib64/libpthread_nonshared.a
RUN ln -s ${SYSROOT}/lib64/libc.so.6 /lib64/libc.so.6
RUN ln -s ${SYSROOT}/usr/lib64/libc_nonshared.a /usr/lib64/libc_nonshared.a

RUN make install

WORKDIR /opt/test
RUN bmi-test pymt_heatc:HeatModel --config-file=../babelizer/docs/source/examples/config.txt --root-dir=. -vvv

RUN conda install -c conda-forge pymt

WORKDIR /opt/babelizer/docs/source/examples
RUN cp info.yaml run.yaml parameters.yaml heat.txt /opt/pymt_heatc/meta/HeatModel
RUN cp pymt_heatc_ex.py /opt/test

WORKDIR /opt/test
RUN sed -i.bak 36s@^@#@ pymt_heatc_ex.py  # a bug in pymt or the babelizer template
RUN python pymt_heatc_ex.py
