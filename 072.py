# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:23:31 2015

@author: gibon
"""

import sympy
import numpy as np

def totient(N):
    return int(N * np.prod([(1-1/p) for p in sympy.factorint(N).keys()]))

def mu(N):
    powers = sympy.factorint(N).values()
    if sum(k > 1 for k in powers):
        return 0
    return (-1) ** sum([k for k in powers])

# n = sum([totient(i) for i in range(2,10**6+1)])

# Even better, from https://en.wikipedia.org/wiki/Euler%27s_totient_function#Other_formulae_involving_.CF.86

# sum([totient(i) for i in range(1,n)]) =
# 1/2 * (1 + sum([mu(i) * int(n/i)**2 for i in range(1,n)]))

def totient_sum(n):
    i = 1
    s = 0
    while i <= n/2:
        s += mu(i) * int(n/i) ** 2
        i += 1
    print(i,s)
    while i <= n:
        s += mu(i)
        i += 1
    return 1/2 * (1 + s)

n = totient_sum(10**6) - 1

print('Solution to problem 72 is %i.'%n)

# Alternative solution from the website
limit = 1000000
phis = [i for i in range(limit + 1)]
primes = [True for i in range(limit + 1)]

primes[0] = primes[1] = False

for i in range(2, limit + 1):
    if primes[i]:
        phis[i] = i - 1
    
        for j in range(i + i, limit + 1, i):
            phis[j] *= (i - 1) / i
            primes[j] = False

# -1 for phi(1)
print(int(sum(phis)) - 1)