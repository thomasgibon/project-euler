# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 00:17:39 2015

@author: gibon
"""

sols = []

for k in range(2,100):
    for p in range(2,9):
        if sum(map(int,list(str(k**p)))) == k:
            sols.append((k**p,k,p))

sols.sort()

n = sols[29][0]

print('Solution to problem 119 is %i.'%n)