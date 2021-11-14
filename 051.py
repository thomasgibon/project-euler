# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:29:19 2015

@author: gibon
"""

import string
from collections import Counter
import itertools

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n # initializes
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1) # i square and all subsequent multiples of i
    return [2] + [i for i in range(3,n,2) if sieve[i]]

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

lb = 56993
ub = 1000000
same = 3

primes = rwh_primes(ub)

#Compile list of primes with three same digits
primes3 = []
digs = string.digits
p_count = dict()
m_count = dict()

for p in primes:
    
    n_count = [str(p).count(k) for k in digs]
    n_3     = [k >= same for k in n_count]
    
    if sum(n_3):
        D = str(n_3.index(1))
        options = [d if d != D else (D,'x') for d in str(p)]
        l = [e for e in list(''.join(o) for o in itertools.product(*options)) if e.count('x') == same]
        primes3.extend(l)
        
        for e in l:
            
            if e in p_count.keys():
                p_count[e] += 1
                if p_count[e] == 8:
                    win = e
                    break
            else:
                p_count[e] = 1
                m_count[e] = p

n = m_count[win]

print('Solution to problem 51 is %i.'%n)