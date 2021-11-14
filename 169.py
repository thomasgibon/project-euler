# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:56:12 2019

@author: Gibon
"""

import numpy as np
import re

p = 14

def dec2bin(p):
    
    max_power = int(np.log2(float(p)))
    
    binary_terms = ''
    
    for k in range(max_power,-1,-1):
        binary_terms += str(p // 2**k)
        p = p % 2**k
    
    return binary_terms

# when in binary, all combinations for potential partitions are the amount of
# ways you can replace '10' by '02' and '20' by '12', recursively
# e.g. 10 is 1010, or 0210, or 0202, or 0112, or 1002
    
# actually, each block of 1 and n zeros can be written in n different ways
# e.g. 8 is 1000 can be written as 0200, 0120, or 0112
# and 16 can be written 10000, 02000, 01200, 01120, or 01112
    

def count_partitions2(p):
    ones = [m.start() for m in re.finditer('10',dec2bin(p))]
    blocks = ['1' + z for z in dec2bin(p).split('1')]
    twenties = [m.start() for m in re.finditer('20',dec2bin(p))]
    