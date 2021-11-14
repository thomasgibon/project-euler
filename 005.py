# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:54:55 2015

@author: gibon
"""

import numpy as np
from fractions import gcd

def lcm(a,b):
    return a*b/gcd(a,b)

l = np.arange(1,21)
n = 1

for i in l:
    n = lcm(i,n)

print('Solution to problem 5 is %i.'%n)