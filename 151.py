# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:33:21 2016

@author: gibon
"""

import numpy as np


cutnuse = {8:[4,2,1],
           4:[2,1],
           2:[1],
           1:[]}
     
p_list = []
      
for i in range(20000):
    
    batch   = [8, 4, 2, 1]
    c = 0
    
    while batch:
        if len(batch) == 1:
            c += 1
            if batch != [1]:
                print(batch)
        pick = batch.pop(np.random.randint(0,len(batch)))
        batch.extend(cutnuse[pick])
    p_list.append(c-1)

print(np.mean(p_list))