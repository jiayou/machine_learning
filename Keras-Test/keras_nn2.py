# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:40:30 2017


Use CNN model against MNIST dataset.
Target:  Correctness > 99%

Advanced topics over CNN
1) expanded data set (nudge, rotate, ...)
2) summary of predict result, error plot, etc

"""

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D, Dropout

import numpy as np
import matplotlib.pyplot as plt

import datetime


#%% Model
model = Sequential()
model.add(Conv2D(16,(3,3),input_shape=(28, 28, 1)))
model.add(MaxPooling2D())
model.add(Conv2D(64,(3,3),input_shape=(13, 13, 1)))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(64))
model.add(Dropout(0.5))
model.add(Activation("relu"))
model.add(Dense(units=10))
model.add(Activation("softmax"))

# model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.summary()


#%% Load Data
import datasets
(train_lbl, train_img) = datasets.mnist_get_train_data_expanded()
(val_lbl, val_img) = datasets.mnist_get_test_data()


#%% Fit

tensor_shape_train = list(train_img.shape)
tensor_shape_train.append(1)
tensor_shape_test  = list(val_img.shape)
tensor_shape_test.append(1)

length_train = tensor_shape_train[0]
length_test  = tensor_shape_test[0]

X_train = train_img.reshape(tensor_shape_train) /255
X_test = val_img.reshape(tensor_shape_test) /255

Y_train = np.zeros([length_train, 10], dtype='uint8');
for i in range(length_train):
    Y_train[i,train_lbl[i]]=1

Y_test = np.zeros([length_test, 10], dtype='uint8');
for i in range(length_test):
    Y_test[i,val_lbl[i]]=1

#
#model.train_on_batch(X_train, Y_train)
hist = model.fit(X_train, Y_train, shuffle=True, 
                 epochs = 5,
                 validation_split=0.2, 
                 validation_data=(X_test, Y_test),
                 batch_size=200)

result = model.evaluate(X_test, Y_test)
print('\n\n')
print(result)

#%% Test
Y_predict = model.predict(X_test, batch_size=32, verbose=0)
predict_lbl = Y_predict.argmax(1)
errors = np.where(predict_lbl != val_lbl)
mismatch = errors[0]
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

#%% execute_and_record():
time_str = str(datetime.datetime.now())

with open(time_str+'_log.txt', 'w') as file:
    file.write(time_str+'\n')
    file.write('Error:'+str(mismatch.size)+'\n\n')

plt.figure(1).set_size_inches(8, 6)
plt.figure(1).savefig(time_str+'_err.png')

plt.figure(2).set_size_inches(8, 6)
plt.figure(2).savefig(time_str+'_tbl.png')

for fig in plt.get_fignums():
    plt.close(fig)
    
    