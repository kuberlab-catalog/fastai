import argparse
from os import path
import tempfile

import torch
from fastai import *
from fastai.vision import *

from mlboardclient.api import client

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--train-dir',
        required=True,
        help='Directory containing the results of training'
    )
    return parser.parse_args()


def main():

    m = client.Client()

    args = parse_args()
    data_dir = path.join(args.train_dir, 'mnist_sample')
    data_path = untar_data(URLs.MNIST_SAMPLE, fname=tempfile.mktemp(), dest=data_dir)
    m.update_task_info({'data_path': str(data_path)})
    print('Using path %s' % data_path)

    data = ImageDataBunch.from_folder(data_path, ds_tfms=(rand_pad(2, 28), []), bs=64)
    data.normalize(imagenet_stats)

    learn = create_cnn(data, models.resnet18, metrics=accuracy)
    learn.fit_one_cycle(1, 0.01)
    print('Accuracy %s' % str(accuracy(*learn.get_preds())))
    m.update_task_info({'accuracy': str(accuracy(*learn.get_preds()))})

    model_location = path.join(args.train_dir, "model")
    model_location = learn.save(model_location, return_path=True)
    print('Model saved to %s' % model_location)
    m.update_task_info({'model_location': str(model_location)})

    print('Network structure:')
    learn.model.eval()


if __name__ == '__main__':
    main()
