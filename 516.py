# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:37:43 2015

@author: gibon
"""

from sympy import totient, factorint
from itertools import islice, chain, tee
 
def merge(r, s):
    # This is faster than heapq.merge.
    rr = next(r)
    ss = next(s)
    while True:
        if rr < ss:
            yield rr
            rr = next(r)
        else:
            yield ss
            ss = next(s)
 
def p(n):
    def gen():
        x = n
        while True:
            yield x
            x *= n
    return gen()
 
def pp(n, s):
    def gen():
        for x in (merge(s, chain([n], (n * y for y in fb)))):
            yield x
    r, fb = tee(gen())
    return r
 
def hamming(a, b = None): # from http://rosettacode.org/wiki/Hamming_numbers#Python
    if not b:
        b = a + 1
    seq = (chain([1], pp(5, pp(3, p(2)))))
    return list(islice(seq, a - 1, b - 1))
 
def is_hamming(n):
    if n == 1:
        return False
    return max(factorint(n).keys()) <= 5

def S(L):
    hamming_numbers = hamming(1, L + 1)
    s = 3 # we count 1 and 2
    for n in range(3,L + 1):
        if totient(n) in hamming_numbers:
            s += n
    return s

L   = 100
ub = 5000
n_ham = hamming(1,ub).index(min(hamming(1,ub), key=lambda x:abs(x-L))) + 1

print("%i is the %ith Hamming number." % (L,n_ham))

print(S(L))



