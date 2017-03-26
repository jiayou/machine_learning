#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:32:38 2017

@author: jiayou

TODO:
3) the filters: how did it work? CNN visualization

    
"""
import numpy as np
import matplotlib.pyplot as plt

from keras.models import load_model
#from image_conv import conv
from datasets import mnist_get_test_data

def foo():
    print('hello')


def conv(img2d, kernel):
    [m,n] = img2d.shape
    [u,v] = kernel.shape
    
    row = m-u+1
    col = n-v+1
    
    kernel_center_y = np.int((u)/2)
    kernel_center_x = np.int((v)/2)
    
#    print(kernel_center_y, kernel_center_x)
    
#    target = np.zeros(target_size)
    padding = np.zeros((m+u-1,n+v-1))
    padding[kernel_center_x:kernel_center_x+n, kernel_center_y:kernel_center_y+m] = img2d
    img = [[ np.sum(padding[i:i+u, j:j+v] * kernel) for j in range(n)  ] for i in range(m)]
#    img = None
    return np.array(img)

def normalize(x):
    low_value = np.min(x)
    high_value = np.max(x)
    return (x-low_value) * 255 / (high_value-low_value)
    
    
#%% MAIN
if __name__ == '__main__':
    
    file_name = '2017-03-25 23:41:33.397518'
    model_hdf = file_name + '_model.h5'
    
    model = load_model(model_hdf)
    model.summary()

    val_lbl, val_img = mnist_get_test_data()
    img2d = val_img[0]

    
    #%%
    l1 = model.get_layer('conv2d_144')
    L1W, L1b = l1.get_weights()
    
    l2 = model.get_layer('conv2d_145')   
    L2W, L2b = l2.get_weights()

    l1_kernel_size = list(L1W.shape)
    l2_kernel_size = list(L2W.shape)

    
    #%% L1 kernels
    L1_kernels = [[L1W[:,:,i,j] 
                for j in range(l1_kernel_size[-1])] 
                for i in range(l1_kernel_size[-2])]
    
#    L1_filters = [x.reshape(3,3) for x in L1_kernels]
#    L1_filters = np.array(L1_kernels)
    
    img_filtered = [[ conv(img2d, filt) for filt in col ] for col in L1_kernels ]
    img_normalized = [[normalize(img) for img in col ] for col in img_filtered]
    
    mm = np.bmat(img_normalized)
    fig1 = plt.figure(1)
    ax1 = plt.subplot(111)
    ax1.imshow(mm, 'Greys')


#%% L2 kernels

    L2_kernels = [[L2W[:,:,i,j] 
                for j in range(l2_kernel_size[-1])] 
                for i in range(l2_kernel_size[-2])]

    img_filtered = [[ conv(img2d, filt) for filt in col ] for col in L2_kernels ]
    img_normalized = [[normalize(img) for img in col ] for col in img_filtered]
    
    mm = np.bmat(img_normalized)
    fig2 = plt.figure(2)
    ax2 = plt.subplot(111)
    ax2.imshow(mm, 'Greys')

#%% L1 conbines L2 kernels

    L1L2_kernels = [[(L1W[:,:,0,i], L2W[:,:,i,j]) 
                for j in range(l2_kernel_size[-1])] 
                for i in range(l2_kernel_size[-2])]

    img_filtered = [[ conv(conv(img2d, f1f2[0]), f1f2[1]) for f1f2 in col ] for col in L1L2_kernels ]
    img_normalized = [[normalize(img) for img in col ] for col in img_filtered]
    
    mm = np.bmat(img_normalized)
    fig3 = plt.figure(3)
    ax3 = plt.subplot(111)
    ax3.imshow(mm, 'Greys')

