# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:08:03 2015

@author: gibon
"""

ub = 1000

c  = [1] + [2] * ub

# http://mathworld.wolfram.com/Convergent.html

h = [0,1]
k = [1,0]

for i in range(len(c)):
    a = c[i]
    h.append(a * h[i + 1] + h[i])
    k.append(a * k[i + 1] + k[i])

h = h[2:]
k = k[2:]

n = sum([len(str(x)) > len(str(y)) for x,y in zip(h,k)])

print('Solution to problem 57 is %i.'%(n))