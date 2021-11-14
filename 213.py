#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:51:38 2019

@author: thomas
"""

import numpy as np

def generate_markov(size):
    
    M = np.zeros([size*size, size*size])
    
    # line by line
    for i in range(size):
        for j in range(size):
            # corner case
            if (i == 0 or i == size-1) and (j == 0 or j == size-1):
                
                m = np.zeros([size,size])
                
                m[i-1,j] = 1./2 * (i > 0)
                m[(i+1)%size,j] = 1./2 * (i < size-1)
                m[i,j-1] = 1./2 * (j > 0)
                m[i,(j+1)%size] = 1./2 * (j < size-1)
                
                M[size*j + i,:] = m.flatten()
                
            # edge case
            elif (i == 0 or i == size-1) or (j == 0 or j == size-1):               
                
                m = np.zeros([size,size])
                
                m[i-1,j] = 1./3 * (i > 0)
                m[(i+1)%size,j] = 1./3 * (i < size-1)
                m[i,j-1] = 1./3 * (j > 0)
                m[i,(j+1)%size] = 1./3 * (j < size-1)
                
                M[size*j + i,:] = m.flatten()
                
            # otherwise
            else:
                
                m = np.zeros([size,size])
                
                m[i-1,j] = 1./4
                m[i+1,j] = 1./4
                m[i,j-1] = 1./4
                m[i,j+1] = 1./4
                
                M[size*j + i,:] = m.flatten()
    return M

M = generate_markov(30)

MM = 1-M
M50 = np.linalg.matrix_power(M,50)

solution = (1-M50).prod(0).sum()
