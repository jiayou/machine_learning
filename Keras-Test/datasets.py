#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:00:30 2017

@author: jiayou
"""


import numpy as np
import gzip, struct

def read_data(label_url,image_url):
    with gzip.open(label_url) as flbl:
        magic, num = struct.unpack(">II",flbl.read(8))
        label = np.fromstring(flbl.read(),dtype=np.int8)
    with gzip.open(image_url,'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII",fimg.read(16))
        image = np.fromstring(fimg.read(),dtype=np.uint8).reshape(len(label),rows,cols)
    return (label, image)

def mnist_get_train_data():
    (train_lbl, train_img) = read_data('datasets/mnist/train-labels-idx1-ubyte.gz','datasets/mnist/train-images-idx3-ubyte.gz')
    return train_lbl, train_img

def mnist_get_test_data():
    (val_lbl, val_img) = read_data('datasets/mnist/t10k-labels-idx1-ubyte.gz','datasets/mnist/t10k-images-idx3-ubyte.gz')
    return val_lbl, val_img

def mnist_get_train_data_expanded():
    from expand_dataset import expanded_mnist_dataset
    return expanded_mnist_dataset()

