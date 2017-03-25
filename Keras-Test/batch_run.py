#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 00:04:07 2017

@author: jiayou
"""

import keras_nn2, result_analysis
import datetime
import matplotlib.pyplot as plt

from IPython.utils import io


#    with io.capture_output() as captured:
    keras_nn2.keras_nn2()
        #execfile('result_analysis.py')

#    print (captured.stdout)
    
    

        

if __name__ == '__main__':
    for i in range(5):
        print('Running Loop ', i)
        execute_and_record()

