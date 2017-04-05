#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:19:16 2017

"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from datasets import mnist_get_train_data, mnist_get_test_data

def image_variants(img2d, R=1):

    im1 = np.zeros(img2d.shape, dtype='uint8')
    im2 = np.zeros(img2d.shape, dtype='uint8')
    im3 = np.zeros(img2d.shape, dtype='uint8')
    im4 = np.zeros(img2d.shape, dtype='uint8')
    im5 = np.zeros(img2d.shape, dtype='uint8')
    im6 = np.zeros(img2d.shape, dtype='uint8')
    im7 = np.zeros(img2d.shape, dtype='uint8')
    im8 = np.zeros(img2d.shape, dtype='uint8')
    
    im0                         =   img2d
    im1[  0:-R    ,    :    ]   =   img2d[  R:    ,   :   ]
    im2[  R:      ,    :    ]   =   img2d[  0:-R  ,   :   ]
    im3[  :       ,   0:-R  ]   =   img2d[  :    ,   R:   ]
    im4[  :       ,   R:    ]   =   img2d[  :    ,   0:-R ]
    im5[  0:-R    ,   0:-R  ]   =   img2d[  R:    ,  R:   ]
    im6[  R:      ,   R:    ]   =   img2d[  0:-R  ,  0:-R ]
    im7[  R:      ,   0:-R  ]   =   img2d[  0:-R  ,  R:   ]
    im8[  0:-R    ,   R:    ]   =   img2d[  R:    ,  0:-R ]

    img10 = Image.fromarray(im0)
    img11 = img10.rotate(10)
    img12 = img10.rotate(-10)
    img13 = img10.rotate(20)
    img14 = img10.rotate(-20)
    
    im11 = np.array(img11)
    im12 = np.array(img12)
    im13 = np.array(img13)
    im14 = np.array(img14)
    
    return [im0, im1, im2, im3, im4, im5, im6, im7, im8, im11, im12, im13, im14]


def expand_dataset(label_set, image_set):
    NUM_VARIANTS = 13
    label_size = list(label_set.shape)
    image_size = list(image_set.shape)
    label_size[0]*=NUM_VARIANTS
    image_size[0]*=NUM_VARIANTS          
    
    expanded_label = [np.zeros(NUM_VARIANTS) + lbl for lbl in label_set]
    expanded_image = [image_variants(img2d) for img2d in image_set]
    
    new_label_set = np.reshape(expanded_label, label_size)
    new_image_set = np.reshape(expanded_image, image_size)
    
    return new_label_set, new_image_set

def test_image_variants0():
    img=np.array(list(range(9)), dtype='uint8').reshape((3,3))
    k = image_variants(img)
    print(k)

def test_image_variants(img):
    variant_list = image_variants(img)
    ax = plt.subplot(111)
    mm = np.bmat(variant_list)
    ax.imshow(mm, 'Greys')
    
def expanded_mnist_dataset():
    (train_lbl, train_img) = mnist_get_train_data()
    return expand_dataset(train_lbl, train_img)
    
if __name__=='__main__':

    # test_image_variants0()

    #% Load Data
    (val_lbl, val_img) = mnist_get_test_data()
    # test_image_variants(val_img[0])

    new_lbl, new_img = expand_dataset(val_lbl, val_img)
    for loops in range(10):
        idx = np.random.randint(0, new_lbl.size, 10)
        fig = plt.figure()
        mm = np.hstack(new_img[idx])
        plt.imshow(mm, 'Greys')
        plt.xlabel(new_lbl[idx])
        