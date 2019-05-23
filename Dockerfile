FROM kuberlab/pytorch:1.0.0-cpu-py3

RUN pip install dataclasses && conda install -c pytorch -c fastai fastai

