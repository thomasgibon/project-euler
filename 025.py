# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:44:04 2015

@author: gibon
"""

f1 = 1
f2 = 2

i = 3

while len(str(f2)) < 1000:
    i += 1
    f3 = f2 + f1
    f1 = f2
    f2 = f3

n = i

print('Solution to problem 25 is %i.'%n)