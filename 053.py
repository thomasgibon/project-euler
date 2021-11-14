# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:25:42 2015

@author: gibon
"""

from math import factorial as fact

def C(n,r):
    if isinstance(r,int) and isinstance(n,int):
        return int(fact(n)/(fact(r)*fact(n-r)))

s = 0

for n in range(101):
    for r in range(n):
        if C(n,r) > 10**6:
            s += 1

n = s

print('Solution to problem 87 is %i.'%n)