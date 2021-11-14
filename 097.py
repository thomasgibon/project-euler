# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 00:39:56 2015

@author: gibon
"""

i = 2
p = 1

while p < 7830457:
    p += 1    
    i *= 2
    i = int(str(i)[-10:])

n = int(str(28433*i)[-10:]) + 1

print('Solution to problem 97 is %i.'%n)