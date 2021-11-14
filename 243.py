# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:32:15 2015

@author: gibon
"""

from sympy import totient, factorint, primorial, prime
from fractions import Fraction

def R(n):
    return Fraction(totient(n),(n-1))

M = Fraction(15499,94744)

k      = 2
r      = R(k)
r_min  = r
k_min  = k

r_list = [r]
k_list = [k]

while r > M:
    if k%1000 == 0:
        print(k)
    k += 1
    r = R(k)
    
    if r < r_min:
        r_min = r
        k_min = k
        r_list.append(r)
        k_list.append(k)

"""
We see that the numbers with low resilience are the primorials and their
multiples
"""

k_list = []

for i in range(1,100):
    p = primorial(i)
    for q in range(1,prime(i + 1)):
        k_list.append(q * p)

i = 0

while r > M:
    
    i += 1
    r = R(k_list[i])

n = k_list[i]

print('Solution to problem 243 is %i.'%n)