# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:11:06 2015

@author: gibon
"""

import numpy as np

l = np.arange(100,1000)
palindroms = []

for i in range(l.size):
    k = l[i] * l[1:i]
    palindroms.append([(l[i],n) for n in k if str(n)[::-1] == str(n)])
    i += 1

products = sorted(set(sum(palindroms,[])), key = lambda p: p[1])

k = products[-1][0]
n = products[-1][1]

print('Solution to problem 4 is %i, product of %i and %i.'%(n,k,n/k))