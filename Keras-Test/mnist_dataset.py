# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:19:59 2017

@author: L-wxia1
"""

import numpy as np
import os
import urllib
import gzip
import struct


def read_data(label_url, image_url):
    with open(label_url, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        label = np.fromstring(flbl.read(), dtype=np.int8)
    with open(image_url, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        image = np.fromstring(fimg.read(), dtype=np.uint8).reshape(len(label), rows, cols)
    return (label, image)


def load_data():
    path=r"C:\WinPython\notebooks\tmp\data\MNIST\\"
    (train_lbl, train_img) = read_data(
        path+'train-labels.idx1-ubyte', path+'train-images.idx3-ubyte')
    (val_lbl, val_img) = read_data(
        path+'t10k-labels.idx1-ubyte', path+'t10k-images.idx3-ubyte')
    
    return train_lbl, train_img, val_lbl, val_img

def sample_plot(train_lbl, train_img):
    import matplotlib.pyplot as plt
    for i in range(10):
        plt.subplot(1,10,i+1)
        plt.imshow(train_img[i], cmap='Greys_r')
        plt.axis('off')
    plt.show()
    print('label: %s' % (train_lbl[0:10],))

if __name__=="__main__":
    train_lbl, train_img, val_lbl, val_img = load_mnist()
    sample_plot(train_lbl, train_img)
