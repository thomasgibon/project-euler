# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:10:24 2015

@author: gibon
"""

from math import factorial as fact
import matplotlib.pyplot as plt
import numpy as np

"""
We can look here http://mathworld.wolfram.com/Dice.html
Use a generating function, or directly:

k_max = int((p - n)/s)
P(p,n,s) = 1/s**n * sum((-1) ** k * C(n,k) * C(p - s*k - 1, n - 1) for k in range(k_max + 1))
"""

sums = range(36 + 1)

def C(n,r): # Combinations
    if n < 0 or r < 0 or n < r:
        return 0
    if isinstance(r,int) and isinstance(n,int):
        return int(fact(n)/(fact(r)*fact(n-r)))

def P(p,n,s):
    """
    Probability of getting the sum p with n dice of s faces
    """
    k_max = int((p - n)/s)
    return 1/s**n * sum((-1) ** k * C(n,k) * C(p-s*k-1, n-1) for k in range(k_max + 1))

Pete  = [P(p,9,4) for p in sums]
Colin = [P(p,6,6) for p in sums]

plt.plot(sums, Pete)
plt.plot(sums, Colin)

"""
For every possible score k,
Pete wins if he scores it or more
AND Colin scores k - 1 or less
"""

n = round(sum([sum(Colin[:k]) * Pete[k] for k in range(0,37)]),7)

print('Solution to problem 205 is %.7f.'%n)