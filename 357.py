# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 00:10:35 2015

@author: gibon
"""

import numpy as np
import time

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

# From http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
    
ub  = 100000000
s   = 0
l   = set()

# Only even nums can be in results
primes = get_primes(ub)
ran = [p - 1 for p in primes if (p - 1)%2 == 0]

start_time = time.time()

while ran != []:
    exitFlag = False
    a = ran.pop()
    i = 1
    div = set()
    while i <= int(a**0.5) and not exitFlag:
        i += 1
        if a % i == 0 and not isprime(i + a/i):
            exitFlag = True
            break
    if not exitFlag:
        l.add(a)
                
print("--- %s seconds ---" % (time.time() - start_time))

n = sum(l) + 1