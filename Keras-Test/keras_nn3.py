#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:19:16 2017

Advanced topics over CNN
1) expanded data set (nudge, rotate, ...)
2) summary of predict result, error plot, etc
3) the filters: how did it work?

"""


from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D, Dropout

