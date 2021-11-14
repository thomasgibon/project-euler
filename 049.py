# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:34:31 2015

@author: gibon
"""

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n # initializes
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1) # i square and all subsequent multiples of i
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes = [p for p in rwh_primes(10000) if len(str(p)) == 4]

for p in primes:
    perms = [perm for perm in primes if sorted(list(str(perm))) == sorted(list(str(p)))]
    if len(perms) >= 3:
        delta = [perm - p for perm in perms]
        dups = [d for d in delta if -d in delta and d != 0]
        if dups != []:
            s = (p+dups[0],p,p-dups[0])
    
n = int(''.join([str(k) for k in s]))

print('Solution to problem 49 is %i.'%n)