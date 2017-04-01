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

logging.basicConfig(level=logging.DEBUG)

#%% 

from keras.models import Sequential
from keras.layers import LSTM, Activation
model = Sequential()
model.add(LSTM(32, input_shape=(4, 64), return_sequences=True))
model.add(Activation('relu'))
model.add(LSTM(8, return_sequences=True))
model.add(Activation('relu'))
model.add(LSTM(4))
model.add(Activation('softmax'))
model.compile(optimizer='sgd', loss='mse')
model.summary()



#%% visualization
from time import sleep
from _thread import start_new_thread

if __name__ == '__main__1':

    
    game = GreedySnakeGame()
    
    start_new_thread(GreedySnakeGameGUI, (game, None))
#    gui(game)
    
    score=0
    while True:
        
        print (game.score)
        score = game.score
        sleep(0.5)
        
    
