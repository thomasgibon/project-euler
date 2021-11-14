# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:09:12 2015

@author: gibon
"""

import numpy as np
import itertools as it

l = np.arange(1,999.)

sets = [comb for comb in it.combinations(l,2) if sum(comb) <= 999]

# The problem simplifies to
# 2000 (a+b) - 2 ab = 1000**2

for (a,b) in sets:
    if 2000 * (a+b) - 2 * a * b == 1e6:
        print(a,b,1000-a-b)
        n = a*b*(1000-a-b)

print('Solution to problem 9 is %i.'%n)