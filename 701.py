# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:43:32 2020

@author: Gibon

https://www.geeksforgeeks.org/check-binary-string-0-between-1s-not/
https://www.geeksforgeeks.org/length-longest-consecutive-1s-binary-representation/
"""

import networkx as nx
import numpy as np

def max_consecutive_ones(x, bits=4):
    
    pattern = '{:0' + str(bits) + 'b}'
    s = pattern.format(x)
    
    if set(s) == {'1'}:
        return len(s)
    
    # prepare s
    while s[-1] == s[0] == '1':
        s = s[-1] + s[:-1]
    
    x = int(s,2)
    
    # Initialize result 
    count = 0
       
    # Count the number of iterations to 
    # reach x = 0. 
    while x!=0: 
      
        # This operation reduces length 
        # of every sequence of 1s by one. 
        x = (x & (x << 1)) 
   
        count += 1
      
    return count 

def generate_edges(shape=(2,2)):
    
    M = np.zeros([shape[0]*shape[1],
                  shape[0]*shape[1]])
    
    # line by line
    for i in range(shape[0]):
        for j in range(shape[1]):
            
            m = np.zeros(shape)
            
            if i>0:
                m[i-1,j] = 1
            if j>0:
                m[i,j-1] = 1
            if i < shape[0]-1:
                m[i+1,j] = 1
            if j < shape[1]-1:
                m[i,j+1] = 1
            
            print(m)
            
            M[i*shape[1] + j,:] = m.flatten()
            
            print(M)
    
    return M

M = generate_edges(shape=(3,4))
G = nx.from_numpy_array(M)
#nx.draw(G)

values = np.array([[1,1,0,0,
                    1,1,0,0,
                    1,0,0,0]])

np.multiply(values,M)

nx.draw(nx.from_numpy_array(values*M*values.T))
