# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:54:55 2017

@author: l-wxia1
"""

import numpy as np
from tictoc import tic, toc
import mnist_dataset
from numpy import vectorize 
from layer import Layer

f = lambda x : 1/(1+np.exp(-x))
df =lambda f: f*(1-f)

sigmoid = vectorize(f)

import logging
logger = logging.getLogger(__name__)

train_lbl, train_img, val_lbl, val_img = mnist_dataset.load_data()

L1 = Layer(28*28, 128, name ="Layer1")
L2 = Layer(128,10, name= "Layer2")

#%% train

#print(train_lbl)

#x0= np.array([1,2,3,4])[np.newaxis].T
#y0= np.array([3,4])[np.newaxis].T

dim = train_lbl.size
tic()
for i in range (0,dim):
#    print("========================= Iteration =====================" + str(i))
#    print(L1.W, L1.b)
#    print(L2.W, L2.b)
#    print("========================= Iteration =====================")
    m = train_img[i]
    k = train_lbl[i]
    x0 = np.asarray(m).reshape((28*28,1)) / 255
    y0 = np.zeros([10,1])
    y0[k] = 1
    
#    print("x0\n", x0)
    x1 = L1.feed(x0)
#    print("x1\n", x1)
    x2 = L2.feed(x1)
#    print("x2\n", x2)
#    print("y0\n", y0)
    e2 = L2.bp(y0-x2)
#    print("e2\n", e2)
    e1 = L1.bp(e2)
#    print("e1\n", e1)
    
#%
toc()

tic()

#%% flt
dim = val_lbl.size
correct = 0
for i in range(0,dim):
    m = val_img[i]
    k = val_lbl[i]
    x0 = np.asarray(m).reshape((28*28,1)) / 255
    x1 = L1.feed(x0)
    x2 = L2.feed(x1)

    if x2.argmax() == k :
        correct+=1

print(correct, dim)
toc()
    