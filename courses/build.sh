#!/usr/bin/env bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker build -t kuberlab/fastai:0.7.0 -f $SCRIPT_DIR/Dockerfile .
docker build -t kuberlab/fastai:0.7.0-gpu -f $SCRIPT_DIR/Dockerfile.gpu .

docker push kuberlab/fastai:0.7.0
docker push kuberlab/fastai:0.7.0-gpu
