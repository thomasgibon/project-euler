# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:03:04 2015

@author: gibon
"""

import itertools as it

def perm(k):
    l = [str(i) for i in range(k)]
    n = l
    while max([len(i) for i in n]) <= k + 1:
        n.append([[i + j for i,j in zip([m],l)] for m in n])

m = list(it.permutations(range(10),10))

n = int(''.join([str(k) for k in m[999999]]))

print('Solution to problem 24 is %i.'%n)