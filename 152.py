# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:34:06 2015

@author: gibon
"""

from mpmath import mp
import fractions
import itertools
import collections

def divisors(k):
    divs = []
    i = 1
    while i <= int(k**0.5):
        if k % i == 0:
            divs.append(i)
            divs.append(int(k/i))
        i += 1
    return set(sorted(divs))
    
def factors(k):
    factors = []
    i = 2
    while i <= int(k**0.5):
        while k%i ==0:
            factors.append(i)
            k //= i
        i += 1
    if k > 1:
        factors.append(k)
    return sorted(factors)

def EF(k):
    l = []
    while k != 0:
        p = int(1/k)+1
        k -= 1/p
        l.append(p)
    return l

def EFsq(k):
    l = []
    while k > 0:
        p = int(int(1/k)**.5)
        k -= 1/p**2
        l.append(p)
    return l
        

ub = 45
lb = 2
N = range(lb,ub + 1)
r = []

l1 = [2,3,4,5,7,12,15,20,28,35]
l2 = [2,3,4,6,7,9,10,20,28,35,36,45]
l3 = [2,3,4,6,7,9,12,15,28,30,35,36,45]

sqinvs = [1/k**2 for k in range(lb,ub+1)]

f1 = []
[f1.extend(factors(k)) for k in l1]

f2 = []
[f2.extend(factors(k)) for k in l2]

f3 = []
[f3.extend(factors(k)) for k in l3]

#for i in range(15):
#    L = list(itertools.combinations(N,i))
#    r.append([sum([1/k**2 for k in l]) for l in L])