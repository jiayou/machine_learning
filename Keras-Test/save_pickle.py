#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:54:54 2017

@author: jiayou
"""

import pickle

with open('mnist_dataset_expanded.pkl','rb') as f:
    var_dict = pickle.load(f)
    
with open('mnist_dataset_expanded.pkl', 'wb') as f:
    pickle.dump({'train_lbl_exp':train_lbl, 'train_img_exp':train_img, 'val_lbl':val_lbl, 'val_img':val_img}, f)
    
