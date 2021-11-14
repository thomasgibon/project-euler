# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:08:43 2015

@author: gibon
"""

import mpmath as mp

mp.mp.dps  = 200
smax       = 0
amax, bmax = 0, 0

for a in range(1,101):
    for b in range(1,101):
        s = sum([int(d) for d in str(int(mp.power(a,b)))])
        if s > smax:
            smax = s
            amax = a
            bmax = b

n = smax

print('Solution to problem 56 is %i.'%(n))