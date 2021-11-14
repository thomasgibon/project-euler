# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:34:26 2015

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

ub = 50000000
a_max = int(ub**(1/2)) # Primes won't go above this number
b_max = int(ub**(1/3))
c_max = int(ub**(1/4))

r = [[]]
for x in [rwh_primes(a_max), rwh_primes(b_max), rwh_primes(c_max)]:
    r = [i + [y] for y in x for i in r]
    
sums = sorted([(a**2 + b**3 + c**4,(a,b,c)) for (a,b,c) in r if a**2 + b**3 + c**4 <= ub])

n = len(set([k[0] for k in sums]))

print('Solution to problem 87 is %i.'%n)