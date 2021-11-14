# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:07:41 2015

@author: gibon
"""

from sympy import isprime, factorint
from fractions import gcd
import sympy
import time

def M(n):
    if n < 0 or not isinstance(n, int):
        return False
    if n == 1:
        return 0
    if isprime(n):
        return 1
    k = n
#    if n % 4 == 2:
#        return n/2 + 1
    while True:
        k -= 1
        if k*(k-1) % n == 0:
            return k

start = time.time()
if __name__ == "__main__":
    ub = 10000
    s  = 0
    k  = 0
    while k < ub:
        k += 1
        s += M(k)
print(time.time()-start)

# Tests

# Find m such as x(x-1) = mn for each n

m_list = [(k,(M(k)*(M(k)-1))/k) for k in range(1,100) if M(k) != 1]

# Can we find the x back?

x_list = [(n,(1+(1+4*m*(n))**.5)/2) for n,m in m_list]

# Yes!

# m exists if 1+4mn is a square