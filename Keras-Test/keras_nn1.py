# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:40:30 2017

@author: l-wxia1
"""

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
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


(train_lbl, train_img) = read_data('datasets/mnist/train-labels-idx1-ubyte.gz','datasets/mnist/train-images-idx3-ubyte.gz')
(val_lbl, val_img) = read_data('datasets/mnist/t10k-labels-idx1-ubyte.gz','datasets/mnist/t10k-images-idx3-ubyte.gz')


model = Sequential()
model.add(Dense(input_dim=784, units=64))
model.add(Activation("relu"))
model.add(Dense(units=10))
model.add(Activation("softmax"))

# model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True),
              metrics=['accuracy'])

model.summary()

X_train = train_img.reshape(60000, 784) /255
X_test = val_img.reshape(10000, 784) /255

Y_train = np.zeros([60000, 10]);
for i in range(60000):
    Y_train[i,train_lbl[i]]=1

Y_test = np.zeros([10000, 10]);
for i in range(10000):
    Y_test[i,val_lbl[i]]=1

#
#model.train_on_batch(X_train, Y_train)
hist = model.fit(X_train, Y_train, shuffle=True, validation_split=0.2, batch_size=50)

result = model.evaluate(X_test, Y_test)
print(result)

#%% Test
Y_predict = model.predict(X_test, batch_size=32, verbose=0)
predict_lbl = Y_predict.argmax(1)
errors = np.where(predict_lbl != val_lbl)
mismatch = errors[0]
print('\n\n')
print('Error: ', mismatch.size)

