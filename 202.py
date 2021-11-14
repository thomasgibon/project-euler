# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:08:58 2016

@author: gibon
"""

from sympy import mobius, divisors

precision = 30

"""
Make a grid of points C (imagine a tiling of eqltl triangles).
In that grid, beams go straight and cross lines as they actually reflect in reality.
We count the crossings as reflections.
"""

Cs = []
for p in range(10):
    for q in range(10):
        Cs.append((3/2*p,(q+p%2*1/2)*3**.5))

"""
In that grid, all the points on any horizontal line (y = k/2*3**.5) have the
same number of crossings. Some of them are not valid since they are a repeating
reflecting pattern.

The answer is the sequence:
https://oeis.org/A128115
linked to https://oeis.org/A103221

The Möbius inversion of the number of partitions of n with parts of size 2 and 3.

The number of partitions is very easy:
"""

def A103221(n):
    return int((n+2)/2) - int((n+2)/3)

def A128115(n):
    return sum([mobius(d) * A103221(n/d) for d in divisors(n)])

# 1000001 bounces can be done in 2*A128115((1000001+3)/2) ways

def nbounces(n):
    if n == 1:
        return 1
    else:
        return 2*A128115((n+3)/2)
        

print('Solution to problem 202 is %i.'%nbounces(12017639147))