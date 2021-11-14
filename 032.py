# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:38:11 2015

@author: gibon
"""

import string
import time

start_time = time.time()

digits = set(string.digits[1:])
l = []
sols = set()

for a in range(2,2000):
    b = 1
    s = ''
    while len(s) <= 9:
        c = a*b
        s = str(a) + str(b) + str(c)
        b += 1
        if len(s) == 9 and set(s) == digits:
            sols.add(c)
            l.append((a,b,c))

n = sum(sols)

print("--- %s seconds ---" % (time.time() - start_time))

print('Solution to problem 32 is %i.'%n)