# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 23:46:06 2015

@author: gibon
"""

import numpy as np

def pyth_triples(M): # Returns all triples with a and b <= M
    triples = []
    for m in range(1,int(M**.5)+1):
        for n in range(1,min(m,int(M/(2*m)))):
            triples.append((sorted((m*m-n*n,2*m*n,m*m+n*n)),int(2*m*(m+n))))
    return sorted(triples)

# La longueur L est 2 * m * (m + n), et m < n
# Ce qui donne n < L**.5 / 2

def pyth_triples_from_length(L):
    triples = []
    for n in range(1,int(L**.5/2) + 1):
        if int((n**2 + 2 * L)**.5)**2 == (n**2 + 2 * L):
            m = int(1/2 * ((n**2 + 2 * L)**.5 - n))
            triples.append(sorted((m*m-n*n,2*m*n,m*m+n*n)))
    return sorted(triples)

"""
The question boils down to:
how many unique L = 2 * m * (m + n), m > n > 1, are there
"""
ub = 120
sieve_L = [False] * (ub + 1)
L = 0

while L <= ub:
    for m in range(1,int((L/2)**.5 + 1)):
        for n in range(m%2+1,min(m,int(L/(2*m) - m)),2):
            sieve_L[2*m*(m+n)] = [m*m-n*n,2*m*n,m*m+n*n]
    L += 2