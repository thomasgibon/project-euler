# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:21:57 2015

@author: gibon
"""

r = range(2,101)
powers = []

for a in r:
    for b in r:
        powers.append(a**b)
        powers.append(b**a)

n = len(set(powers))

print('Solution to problem 29 is %i.'%n)