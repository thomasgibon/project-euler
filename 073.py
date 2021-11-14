# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:10:48 2015

@author: gibon
"""

import sympy
import numpy as np
from math import ceil

def listfrac(N):
    l = []
    for d in range(1,N + 1):
        for n in range(1,d):
            l.append(sympy.nsimplify(n/d))
    return sorted(list(set(l)))

def totient(N):
    return N * np.prod([(1-1/p) for p in sympy.factorint(N).keys()])

test = []

for n in range(3,100):
    l = listfrac(n)
    start = l.index(1/3) + 1
    end   = l.index(1/2)

    test.append((n,l[start:end]))

test1 = [(t[0],len(t[1])) for t in test]
test2 = [(test[i][0], set(test[i][1]) ^ set(test[i-1][1])) for i in range(1,len(test))]
test3 = [(test1[i][0],sympy.factorint(test1[i][1] - test1[i-1][1])) for i in range(1,len(test1))]

test4 = []

for i in range(100):
    test4.append((i,(sum([totient(i) for i in range(1,i)]) - 1)/6))