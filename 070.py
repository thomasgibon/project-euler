# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:26:05 2015

@author: gibon
"""

import sympy
import numpy as np

def totient(N):
    return int(N * np.prod([(1-1/p) for p in sympy.factorint(N).keys()]))

# Tout nombre est la somme des indicatrices de ses diviseurs

ub = 10**7

# Make a sieve!
    
phis = list(range(ub))
primes = [True] * ub

primes[0] = primes[1] = False

for i in range(2, ub):
    if primes[i]:
        phis[i] = i - 1
    
        for j in range(i + i, ub, i):
            phis[j] *= (i - 1) / i
            primes[j] = False

r_min = 2
i_min = 0

for i in range(2,ub):
    if i % 10000 == 0:
        print(i)
    if sorted(str(int(phis[i]))) == sorted(str(i)):
        r = i/phis[i]
        if r < r_min:
            r_min = r
            i_min = i