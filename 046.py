# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:30:53 2015

@author: gibon
"""

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

i = 3
notfound = True

while notfound:
    i += 2
    if not isprime(i):
        if sum([isprime(i - 2*sq**2) for sq in range(1,int((i/2)**.5) + 1)]) == 0:
            notfound = False
            n = i
            break

print('Solution to problem 46 is %i.'%n)