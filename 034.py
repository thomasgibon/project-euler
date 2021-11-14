# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:09:38 2015

@author: gibon
"""

import math
import matplotlib.pyplot as plt

a = []
l = []
ub = 2500000

for i in range(3,ub):
    s = sum([math.factorial(int(d)) for d in str(i)])
    l.append(s)
    if s == i:
        a.append(i)

# Check we cover everything with plt.plot(l),plt.plot(range(200))

n = sum(a)

print('Solution to problem 34 is %i.'%n)