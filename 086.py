# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:18:55 2015

@author: gibon
"""

import numpy as np

def part(n,k): # Partitions de n

    if k == 1:
        return 1
        
    if k == 2:
        return int(n/2)
            
    p = np.zeros((n,n))
    
    np.fill_diagonal(p,1)
    p[:,0] = np.ones((1,n))
    
    m = 1
    while m < n:
        i = 1
        while i < m:
            p[m, i] = p[m - 1, i - 1] + p[m - i - 1, i]
            i += 1
        m += 1
    return list(map(int,p[-1,:]))[k-1]

def pyth_triples(M): # Returns all triples with a and b <= M
    triples = []
    for m in range(1,int(M**.5)+1):
        for n in range(1,min(m,int(M/(2*m)))):
            triples.append((sorted((m*m-n*n,2*m*n,m*m+n*n))))
    return sorted(triples)

# Maximum for two sides is 200
triples = [t for t in pyth_triples(200) if t[0] <= 100 or t[1] <= 100]
sum((t[1] for t in triples))

M = 100
sols = []

for a in range(1,M + 1):
    for b in range(1,a + 1):
        for c in range(1,b + 1):
            shortest = (a*a + (b + c)*(b + c))**.5
            
            if int(shortest) == shortest:
                sols.append((a,b,c))
                
M = 10
s = 0

for a in range(1,M + 1):
    for b in range(1,2*a + 1):
        shortest = (a*a + b*b)**.5
        
        if int(shortest) == shortest:
            s += int(a/2) - (a - b - 1)