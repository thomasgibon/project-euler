# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:37:05 2015

@author: gibon
"""

from math import log, ceil
import itertools

sets = []

for b in range(2,1000):
    max_k = int(12 * log(10) / log(b)) + 1
    sets.append(set(int((b**(k + 1) - 1)/(b - 1)) for k in range(max_k)))

strong_repunits = set()

for set_pair in itertools.combinations(sets,2):
    strong_repunits |= set_pair[0] & set_pair[1]

assert sum([k for k in strong_repunits if k < 1000]) == 15864

# Try with while

b = 2

repunits = set()
strong_repunits = set()

ub = 10**12

while b < ub**.5:
    
    if b%10000 == 0:
        print(b)
        
    max_k = ceil(log(ub)/log(b)) # This is only an approximation
    repunits_b = set(int((b**(k + 1) - 1)/(b - 1)) for k in range(max_k))
    
    if max(repunits_b) > ub:
        repunits_b -= {max(repunits_b)}
    
    strong_repunits |= repunits_b & repunits
    strong_repunits |= set(big for big in repunits_b if ub**.5 < big < ub)
    repunits ^= repunits_b
    
    b += 1

n = sum(strong_repunits)

print('Solution to problem 346 is %i.'%n)