# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:18:38 2019

@author: Gibon
"""

from math import ceil
from collections import Counter

# Counting the number of "hollow" square laminae that can form one, two, three, ... distinct arrangements

tiles = 1000000

n_max = int(tiles/4) + 1 # side size
m_max = n_max - 2        # hole size

assert n_max**2 - m_max**2 <= tiles

c = 0

M = {}

for n in range(3,n_max + 1):    
    for m in range(ceil((max(tiles + 1,n*n) - tiles)**.5),n-2 + 1):
        tiles_used = n*n - m*m
        if (tiles_used) % 4 == 0: # if the square difference is zero
            c += 1               # then we can tile
            if tiles_used not in M.keys():
                M[tiles_used] = [(n,m)]
            else:
                M[tiles_used].append((n,m))

L = {k:len(v) for k,v in M.items()}
N = Counter(L.values())

n = sum(v for k,v in N.items() if k in range(1,11))

print('Solution to problem 174 is {}'.format(n))