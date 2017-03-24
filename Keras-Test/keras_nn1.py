# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:40:30 2017

@author: l-wxia1
"""

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
import numpy as np

import mnist_dataset

model = Sequential()

#import theano as T

model.add(Dense(output_dim=64, input_dim=784))
model.add(Activation("sigmoid"))
model.add(Dense(output_dim=10, input_dim=64))
model.add(Activation("sigmoid"))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))

Y_train, X_train, Y_test, X_test = mnist_dataset.load_data()
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

Y_vec = np.zeros([60000, 10]);
for i in range(60000):
    Y_vec[i,Y_train]=1

#
#model.fit(X_train.T, Y_train.T)
model.fit(X_train, Y_vec)

#

#Y_predict = model.predict(X_test)
#print(Y_predict)
