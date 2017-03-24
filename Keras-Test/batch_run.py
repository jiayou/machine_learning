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

def execute_and_record():
    with io.capture_output() as captured:
        keras_nn2.keras_nn2()
        #execfile('result_analysis.py')

    print (captured.stdout)
    
    
    time_str = str(datetime.datetime.now())
    
    with open(time_str+'_log.txt', 'w') as file:
        file.write(captured.stdout)
    
    plt.figure(1).set_size_inches(8, 6)
    plt.figure(1).savefig(time_str+'_err.png')
    
    plt.figure(2).set_size_inches(8, 6)
    plt.figure(2).savefig(time_str+'_tbl.png')
    
    for i in plt.get_fignums():
        plt.close(i)
        

if __name__ == '__main__':
    for i in range(50):
        print('Running Loop ', i)
        execute_and_record()

