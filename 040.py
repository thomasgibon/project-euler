# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:25:50 2015

@author: gibon
"""

import numpy as np

i = 1
d = ''

while len(d) <= 1000000:
    d += str(i)
    i += 1

n = np.prod([int(d[10**i - 1]) for i in range(7)])

print('Solution to problem 40 is %i.'%n)