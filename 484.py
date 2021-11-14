# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:25:14 2015

@author: gibon
"""

from sympy.ntheory import factorint, prime
import sympy
import numpy as np
import matplotlib.pyplot as plt
from fractions import gcd
import time

ub = 5*10**15
ub = 100

def arithmetic_derivative(x):
    if x != int(x): # rational
        (a, b) = sympy.fraction(sympy.nsimplify(x))
        da = np.int64(a * sum([e/p for p, e in factorint(a).items()]))
        db = np.int64(b * sum([e/p for p, e in factorint(b).items()]))
        return (da*b - a*db)/b**2
    else:
        return sum([np.int64(x * e/p) for p, e in factorint(x).items()])

g = [(gcd(x,arithmetic_derivative(x))) for x in range(1,10000)]
plt.plot(g)

# For multiples of square primes, the answer is the number if prime > power
#
# For multiples of prime ** prime, the answer is prime ** prime
#
# For multiples of prime1 ** prime1 * prime2 ** prime2 * ... same

test = [(x, np.prod([p ** (e - (1 - (e % p == 0) * 1)) 
for p, e in factorint(x).items()]), gcd(x, arithmetic_derivative(x)))
for x in range(1,1000)]

# Count the times when it's 4
ub / 2**2

start = time.time()
[factorint(x) for x in range(1000)]
print(time.time() - start)

i = 1

while prime(i) ** prime(i) < ub:
    i += 1

p_max = prime(i-1)

i = 1

while p_max ** i < ub:
    i += 1

d_max = p_max ** (i - 1)