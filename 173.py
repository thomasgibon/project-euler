# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:03:08 2015

@author: gibon
"""

from math import ceil

# Using up to one million tiles how many different "hollow" square laminae can be formed?

tiles = 1000000

n_max = int(tiles/4) + 1 # side size
m_max = n_max - 2        # hole size

assert n_max**2 - m_max**2 <= tiles

c = 0

for n in range(3,n_max + 1):
    if c % 10**4 == 0:
        print(c)
    for m in range(ceil((max(tiles + 1,n*n) - tiles)**.5),n-2 + 1):
        if (n*n - m*m) % 4 == 0: # if the square difference is zero
            c += 1               # then we can tile

n = c

print('Solution to problem 173 is %i.'%n)