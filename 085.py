# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:08:41 2015

@author: gibon
"""

# For a rectangle a × b, the number of rectangles that fit is
# a (a + 1) / 2 * b (b + 1) / 2

def rect(a,b):
    """Ways to arrange rectangles in a a × b rectangle"""
    return a * (a + 1) / 2 * b * (b + 1) / 2

a = 0
arrs = []
ub   = 2000000
amax = int((1 + (1 + 8*ub)**.5)/2) # if b = 1, any further value of a will yield too
                                   # high a result

delta = ub

for a in range(amax):
    r = 0
    b = 0
    while b < a:
        b += 1
        r = rect(a,b)
        d = abs(ub - r)
        if d < delta:
            delta = d
            arrs.append((a,b,r))
            area = a * b

n = area

print('Solution to problem 85 is %i.'%n)