# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:07:34 2015

@author: gibon
"""

import itertools as it

digits = 10

m = [int(''.join([str(i) for i in t])) for t in list(it.permutations(range(0,digits),digits)) if t[5] in (0,5)]
p = [2,3,5,7,11,13,17]
l = len(p)

sols = []

for k in m:
    check = 0
    j = 0
    while check == 0 and j < l:
        j += 1
        check += int(str(k)[j:j+3])%p[j-1]
        if j == l and check == 0 and len(str(k)) == digits:
            sols.append(k)

n = sum(sols)

print('Solution to problem 41 is %i.'%n)