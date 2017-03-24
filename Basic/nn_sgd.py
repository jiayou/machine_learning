# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:54:55 2017

@author: l-wxia1
"""

import numpy as np
from layer import Layer
from tictoc import tic, toc
import mnist_dataset

L1 = Layer(28*28, 64, name ="Layer1")
L2 = Layer(64,10, name= "Layer2")

def epoch(train_x, train_y, epoch_size=100):
    tic()
    for i in range(epoch_size):
        SGD(train_x, train_y)
    toc()
        

def SGD(train_x, train_y, learning_rate=1, mini_batch=100):

    elem = np.random.randint(0, 60000, mini_batch)
    mini_x = train_x[elem,:,:]
    mini_y = train_y[elem]
    
    gradW1 = np.zeros(L1.W.shape)
    gradW2 = np.zeros(L2.W.shape)
    gradb1 = np.zeros(L1.b.shape)
    gradb2 = np.zeros(L2.b.shape)
    
    for i in range(mini_batch):
        m = mini_x[i]
        k = mini_y[i]
        x0 = np.asarray(m).reshape((28*28,1)) / 255
        y0 = np.zeros([10,1])
        y0[k] = 1
    
        x1 = L1.feed(x0)
        x2 = L2.feed(x1)
        dW2, db2, e2 = L2.gradient((y0-x2)/(x2*(1-x2)))     # cross entropy
#       dW2, db2, e2 = L2.gradient(y0-x2)
        dW1, db1, e1 = L1.gradient(e2)
        
#        print(x2.T)
#        print(y0.T)
        
        gradW1 += dW1
        gradW2 += dW2
        gradb1 += db1
        gradb2 += db2
        
    L1.W += gradW1 * learning_rate / mini_batch
    L2.W += gradW2 * learning_rate / mini_batch
    L1.b += gradb1 * learning_rate / mini_batch
    L2.b += gradb2 * learning_rate / mini_batch

#   print(gradW2)
    

def fit(val_img,val_lbl):
	tic()
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

	toc()
	print(correct, dim)

    
train_y, train_x, val_y, val_x = mnist_dataset.load_data()
#train(train_x, train_y)
#fit(val_x, val_y)

for i in range(300):
    print("Epoch", i)
    epoch(train_x, train_y)
    fit(val_x, val_y)
    