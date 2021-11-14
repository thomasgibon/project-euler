# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 20:51:56 2016

@author: Thomas
"""

import numpy as np
import matplotlib.pyplot as plt

def partitionfunc(n,k,l=1):
    '''n is the integer to partition, k is the length of partitions, l is the min partition element size'''
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in range(l,n+1):
        for result in partitionfunc(n-i,k-1,i):
            yield (i,)+result

def layers(abc, l):
    '''
    Returns the number of cubes necessary to cover layer l of the cuboid abc
    '''
    (a,b,c) = abc
    
    if l in (1,2):
        cubes = 2 * (a*b + b*c + a*c) + 4 * (l-1) * (a + b + c)    
    else:
        cubes = 2 * (a*b + b*c + a*c) + 4 * (l-1) * (a + b + c) + 4 * (l-2) * (l-1)
        
    return cubes

def coefs(abc):
    (a,b,c) = abc
    
    A = 4
    B = 4 * (a + b + c) - 12
    C = 2 * (a*b + b*c + a*c) - 4 * (a + b + c) + 8
    
    return (A,B,C)

def coefs_sum_abc(sum_abc):
    ABC  = [(4, 4*sum_abc-12, 2*(a*b+b*c+a*c)+4*sum_abc+8) for (a,b,c) in partitionfunc(sum_abc,3,1)]
    ABCD = [((A,B,C),(B*B-4*A*C)**.5) for (A,B,C) in ABC]
    return ABCD

dims = []

for d in range(50):
    for e in range(1,d+1):
        for f in range(1,e+1):
            dims.append((d,e,f))

sols = []
lays = range(1,10)
cubs = []
C = {}

for abc in dims:
    lay = []
    for l in lays:
        c = layers(abc,l)
        if c in C.keys():
            C[c].append((abc,coefs(abc),l))
        else:
            C[c] = [(abc,coefs(abc),l)]
        lay.append(c)
        sols.append((abc,l,c))
    cubs.append(lay)

print(max(len(c) for c in C.values()))