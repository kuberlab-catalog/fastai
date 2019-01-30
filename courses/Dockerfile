FROM kuberlab/mlbase:cpu-36-full

RUN pip --no-cache-dir install tensorboardX

RUN conda install pytorch==0.3.1 -c pytorch

RUN pip install tensorflow==1.9.0 && \
  pip install fastai==0.7.0 && pip install torchtext==0.2.3

# Install ONNX and onnx-tf for torch -> onnx -> tensorflow conversion
#RUN apt-get update && apt-get install -y \
#  build-essential \
#  cmake \
#  protobuf-compiler \
#  libprotoc-dev && \
#  git clone --recursive https://github.com/onnx/onnx && cd onnx && \
#  python setup.py install && cd .. && rm -rf onnx && \
#  git clone https://github.com/onnx/onnx-tensorflow && \
#  cd onnx-tensorflow && \
#  pip install . && \
#  cd .. && \
#  rm -rf onnx-tensorflow

# Need for passing value from docker build command and it invalidates cache ->
# all commands below must always be executed on every build.
ARG CACHE_DATE=2018-10-10T14:00:00

RUN pip install --no-cache-dir 'git+https://github.com/kuberlab/python-mlboardclient.git'


