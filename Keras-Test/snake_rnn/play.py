# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 10:11:25 2017

@author: L-wxia1
"""


#import PyQt5
#import numpy as np
#from PIL import Image


from game import GreedySnakeGame
from game_view import GreedySnakeGameGUI
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

#%% 

from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense, Dropout

model = Sequential()
model.add(LSTM(32, input_shape=(4, 64), return_sequences=True))
model.add(Activation('relu'))
model.add(LSTM(32, return_sequences=True))
model.add(Activation('relu'))
model.add(LSTM(4))
model.add(Activation('softmax'))
model.compile(optimizer='sgd', loss='mse')
model.summary()

#model = Sequential()
#model.add(Dense(32, input_shape=(64,)))
#model.add(Dropout(0.01)) 
#model.add(Activation('relu'))
#model.add(Dense(4))
#model.add(Activation('softmax'))
#model.compile(optimizer='sgd', loss='mse')
#model.summary()


def discount_reward(r):
    discount_r = np.zeros_like(r)
    running_add=0
    for t in reversed(xrange(0, r.size)):
        if r[t]!=0: running_add=0
        running_add = running_add * gamma * r[t]
        discount_r[t] = running_add
        
    return discount_r
    
def pixels(X):
    return np.reshape(X, (1,64))
    
#%% visualization
from time import sleep
from _thread import start_new_thread

if __name__ == '__main__':

    directions = ('up', 'down', 'left', 'right')
    game = GreedySnakeGame()
    
    start_new_thread(GreedySnakeGameGUI, (game, None))
#    gui(game)
    
    batch_number = 100
    
    score_now = 0
    reward_time_penalty = 0
    live_time = 0
    episode = 0
    pixel_list = np.zeros((4, 64))
    batch_training = True
    game.restart()
    pixel_prev = game.get_info()
    
    while batch_training:
        pixel_now = game.get_info()
        if pixel_prev == pixel_now:
            continue
        else:
            pixel_prev = pixel_now
        
        pixel_list[0:-1,:] = pixel_list[1:,:]   # matrix shift up
        pixel_list[-1,:] = np.reshape(pixel_now, (1,64))
        X = pixel_list.reshape(1,4,64)
        
        prob_y = model.predict(X, batch_size=1)
        y = np.argmax(prob_y)
        game.key_arrow(directions[y])
        Y = np.zeros(4)
        Y[y]=1
        
        if not game.gameover():
            # still alive. small reward.
            logger.error('train on batch')
            live_time += 1
            model.train_on_batch(X, Y.reshape(1,4))
            logger.error('train on batch finish')
            
        else:
            logger.error('restart')
            game.restart()
            episode += 1
            continue

        score_prev = score_now
        score_now = game.get_score()
        if score_now - score_prev > 0:
            # big award
            logger.error('big award')
            
            continue

        if episode >= batch_number:
            break
#            batch_training = False
#            model.train_on_batch()
#            
#            
#        print (game.get_score())
        sleep(0.1)
        
    
