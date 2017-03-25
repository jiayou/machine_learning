#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:05:17 2017

@author: jiayou
"""


def conv(img2d, kernel):
    [m,n] = img2d.shape
    [u,v] = kernel.shape
    
    row = m-u+1
    col = n-v+1
    
    kernel_center_y = np.int((u)/2)
    kernel_center_x = np.int((v)/2)
    
    print(kernel_center_y, kernel_center_x)
    
#    target = np.zeros(target_size)
    padding = np.zeros((m+u-1,n+v-1))
    padding[kernel_center_x:kernel_center_x+n, kernel_center_y:kernel_center_y+m] = img2d
    img = [[ np.sum(padding[i:i+u, j:j+v] * kernel) for j in range(n)  ] for i in range(m)]
#    img = None
    return img
    
def test_conv(val_img):
    p1 = val_img[1]
    new_img = conv(p1, np.array([[2,2,4],[0,0,0],[2,2,2]]))
    z = p1*0
    
    ax=plt.subplot(111)
    ax.grid(True)
    ax.imshow(np.bmat('p1, new_img; new_img, z'), 'Greys')

    #ax.imshow(p1, 'Greys')
