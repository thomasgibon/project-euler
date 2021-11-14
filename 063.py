# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:36:11 2015

@author: gibon
"""

ub = 200

l = []

for k in range(ub):
    i = 1
    while len(str(i**k)) <= k:
        if len(str(i**k)) == k:
            l.append([i,k,i**k])
        i += 1
        
n = i

print('Solution to problem 63 is %i.'%n)