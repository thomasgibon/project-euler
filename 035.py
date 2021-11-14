# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:23:03 2015

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

ub = 1000000

primes = set([i for i in range(ub + 1) if isprime(i)])

sol = set()

for p in primes:
    s = str(p)
    l = len(s)
    perms = set([int(''.join([s[i-j] for i in range(l)])) for j in range(l)])
    if perms <= primes:
        sol |= perms

n = len(sol)

print('Solution to problem 35 is %i.'%n)