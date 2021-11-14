# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:17:07 2015

@author: gibon
"""

from sympy import primefactors, sieve
from math import log

def M_slow(p,q,N):
    
    n = N + 1
    
    while True:
        n -= 1
        if primefactors(n) == [p,q]:
            return n

def M(p,q,N):
    
    if 1 in (p,q):
        if p*q <= N:
            return p*q
        return 0
        
    max_pp = int(log(N/q)/log(p))
    max_n = 0
    
    for pp in range(max_pp,0,-1):
        for qq in range(int(log(N/p**pp)/log(q)),0,-1):
            n = p**pp*q**qq
            if n > max_n and n <= N:
                max_n = n
    return max_n

def S(N):
    
    s_list = []
    
    for p in sieve.primerange(2,int((N/2)**.5) + 1):
        for q in sieve.primerange(p + 1,int(N/p) + 1):
            s_list.append((p,q,M(p,q,N)))
    
    return sum(s[2] for s in s_list), sorted(s_list)

#n = S(10**7)