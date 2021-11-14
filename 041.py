# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:40:06 2015

@author: gibon
"""

import itertools as it

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
        
def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n # initializes
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1) # i square and all subsequent multiples of i
    return [2] + [i for i in range(3,n,2) if sieve[i]]

m = []

for i in range(1,9):
    m.extend([[0] * (9-i) + list(t) for t in list(it.permutations(range(1,i+1),i))])

n = 0

while n == 0:
    l = m.pop()
    p = int(''.join([str(d) for d in l]))
    if isprime(p):
        n = p

print('Solution to problem 41 is %i.'%n)