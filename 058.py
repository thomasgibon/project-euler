# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:38:32 2015

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
        
# Formulae for diagonals
#
# (2 * k)**2 - (2 * k - 1))
# (2 * k)**2 + 1
# (2 * k)**2 + (2 * k - 1)
# (2 * k + 1)**2

#ub = 1000
#
#primes = rwh_primes((2 * ub + 1)**2)

def spiral_diag(k): # k is layer, side is 2 * k + 1
    if k == 0:
        return [1]
    else:
        return [(2 * k)**2 - (2 * k - 1), (2 * k)**2 + 1, (2 * k)**2 + (2 * k + 1), (2 * k + 1)**2]

k = -1
s = 0
notFound = True

while notFound:
    k += 1
    test = [isprime(d) for d in spiral_diag(k)]
    s += sum(test)
    if s/(4 * k + 1) < .1 and k > 1:
        notFound = False
    if k < 10 or k % 1000 == 0:
        print(k, s/(4 * k + 1))

n = 2 * k + 1
 