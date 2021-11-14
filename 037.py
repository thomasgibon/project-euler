# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:20:47 2015

@author: gibon
"""

import string

def isprime(k):
    if k <= 1:
        return False
    elif k == 2:
        return True
    else:
        i = 2
        while i <= int(k**0.5):
            if k % i == 0:
                return False
            i += 1
        return True

primedigits = [d for d in string.digits if isprime(int(d))]
sols = primedigits
truncatable_primes = []

for p in sols:
    for d in string.digits:
        s = p + d
        if isprime(int(s)):# and isprime(int(s[1:])):
            sols.append(s)
            if len(s) > 1 and isprime(int(s[-1])) and isprime(int(s[1:])) and isprime(int(s[-2:])) and s not in truncatable_primes:
                print(s)
                truncatable_primes.append(s)
                
n = sum([int(t) for t in truncatable_primes])

print('Solution to problem 37 is %i.'%n)