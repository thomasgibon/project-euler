# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:40:42 2015

@author: gibon
"""

import mpmath as mp

k = 0
mp.mp.dps = 1000000000

for a in range(1,1001):
    k += int(str(int(mp.power(a,a)))[-10:])

n = int(str(k)[-10:])

print('Solution to problem 48 is %i.'%n)