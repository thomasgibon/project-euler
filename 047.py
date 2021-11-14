# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:53:36 2015

@author: gibon
"""

import numpy as np

def isprime(k):
    if k <= 1:
        return False
    if k == 2:
        return True
    else:
        i = 2
        while i <= int(k**0.5):
            if k % i == 0:
                return False
            i += 1
        return True

def divisors(k):
    divs = []
    i = 1
    while i <= int(k**0.5):
        if k % i == 0:
            divs.append(i)
            divs.append(int(k/i))
        i += 1
    return sorted(divs)

def factors(k):
    factors = []
    i = 2
    while i <= int(k**0.5):
        while k%i ==0:
            factors.append(i)
            k //= i
        i += 1
    if k > 1:
        factors.append(k)
    return sorted(factors)

lb = 0
k = lb
notfound= True

while notfound:
    p = [len(set(factors(j))) == 4 for j in range(k,k+4)]
    if np.prod(p) == 1:
        n = k
        notfound = False
    k += 1
    if k%10000 == 0:
        print(k)

print('Solution to problem 47 is %i.'%n)