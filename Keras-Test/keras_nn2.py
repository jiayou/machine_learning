# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:40:30 2017


Use CNN model against MNIST dataset.
>99%

"""

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D, Dropout

import numpy as np
import matplotlib.pyplot as plt

import gzip, struct
import datetime

def read_data(label_url,image_url):
    with gzip.open(label_url) as flbl:
        magic, num = struct.unpack(">II",flbl.read(8))
        label = np.fromstring(flbl.read(),dtype=np.int8)
    with gzip.open(image_url,'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII",fimg.read(16))
        image = np.fromstring(fimg.read(),dtype=np.uint8).reshape(len(label),rows,cols)
    return (label, image)

def keras_nn2():
    (train_lbl, train_img) = read_data('datasets/mnist/train-labels-idx1-ubyte.gz','datasets/mnist/train-images-idx3-ubyte.gz')
    (val_lbl, val_img) = read_data('datasets/mnist/t10k-labels-idx1-ubyte.gz','datasets/mnist/t10k-images-idx3-ubyte.gz')
    
    
    model = Sequential()
    model.add(Conv2D(16,(3,3),input_shape=(28, 28, 1)))
    model.add(MaxPooling2D())
    model.add(Conv2D(16,(3,3),input_shape=(13, 13, 1)))
    model.add(MaxPooling2D())
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Dropout(0.5))
    model.add(Activation("relu"))
    model.add(Dense(units=10))
    model.add(Activation("softmax"))
    
    # model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])
    
    print(model.summary())
    
    X_train = train_img.reshape(60000,28,28,1) /255
    X_test = val_img.reshape(10000,28,28,1) /255
    
    Y_train = np.zeros([60000, 10]);
    for i in range(60000):
        Y_train[i,train_lbl[i]]=1
    
    Y_test = np.zeros([10000, 10]);
    for i in range(10000):
        Y_test[i,val_lbl[i]]=1
    
    #
    #model.train_on_batch(X_train, Y_train)
    hist = model.fit(X_train, Y_train, shuffle=True, validation_split=0.2, batch_size=100)
    
    res= model.evaluate(X_test, Y_test)
    
    Y_predict = model.predict(X_test, batch_size=32, verbose=0)
    predict_lbl = Y_predict.argmax(1)
    errors = np.where(predict_lbl != val_lbl)
    mismatch = errors[0]
    print('\n\n')
    print('Error: ', mismatch.size)
    
    #%% Table View
    
    error_matrix = [[np.sum(np.logical_and(val_lbl==i, predict_lbl==j)) 
                        for i in range(10)]
                        for j in range(10)]
    
    plt.figure(1)
    ax = plt.subplot(111)
    ax.xaxis.set_visible(True)
    ax.yaxis.set_visible(True)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel('validation')
    ax.set_ylabel('predict')
    ax.set_title(str(mismatch.size))
    ytable = ax.table(cellText = error_matrix,
              colLabels=list(range(10)),
              rowLabels=list(range(10)),
              loc='center',cellLoc='center'
              )
    
    ytable.scale(0.9,1.6)
    
    #%% Figure View
    
    plt.figure(2)
    for i in range(min(100, mismatch.size)):
        ax = plt.subplot(10, 10, i+1)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        idx = mismatch[i]
        img = val_img[idx]
        ax.imshow(img,'Greys')
        ax.text(30, 10,str(val_lbl[idx]))
        ax.text(30, 25,str(predict_lbl[idx]))
    
    
if __name__ == '__main__':
    keras_nn2()
    