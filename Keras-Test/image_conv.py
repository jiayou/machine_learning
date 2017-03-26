#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:05:17 2017

@author: jiayou
"""

import numpy as np

    
def test_conv(val_img):
    p1 = val_img[1]
    new_img = conv(p1, np.array([[2,2,4],[0,0,0],[2,2,2]]))
    z = p1*0
    
    ax=plt.subplot(111)
    ax.grid(True)
    ax.imshow(np.bmat('p1, new_img; new_img, z'), 'Greys')

    #ax.imshow(p1, 'Greys')
