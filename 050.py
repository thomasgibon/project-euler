# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:40:56 2015

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


def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n # initializes
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1) # i square and all subsequent multiples of i
    return [2] + [i for i in range(3,n,2) if sieve[i]]


ub = 1000000
primes = []
i = 0

while sum(primes) < ub:
    i += 1
    primes = rwh_primes(i)

L = len(primes)
notfound = True
s = sum(primes)
sums = []
l = L

while notfound:
    l -= 1
    i = L - l
    while s >= ub and i >= 0:
        t = sum(primes[i:i+l])
        if isprime(t):
            s = t
            s_list = (primes[i:i+l],l,s)
            notfound = False
        i -= 1
        
n = s

print('Solution to problem 50 is %i.'%n)
    