# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 22:03:30 2015

@author: gibon
"""

import numpy as np
from fractions import gcd
import mpmath
 
# The Continued Fraction
def CF(a, f):
    c = []
    for i in range(f):
        c.append(int(a))
        a = 1 / (a - int(a))
    
    return c

def CF_inv(c, f):
    a = c[f]
    for i in c[f - 1::-1]:
        a = i + 1 / a
    return a

ub = 100

c       = [1] * ub
c[0]    = 2
c[2::3] = range(2,2*int(ub/3 + 1),2)

# http://mathworld.wolfram.com/Convergent.html


p_all = []
q_all = []

for k in range(2,ub+1):
    a = np.zeros([k,k], dtype = 'int64')
    for i in range(k):
        a[i,i] = c[i]
        if i < k - 1:
            a[i,i+1] = -1
            a[i+1,i] = 1
    
    b = a[1:,1:]
    
    p,q = mpmath.det(a),mpmath.det(b)
    p_all.append(p/gcd(p,q))
    q_all.append(q/gcd(p,q))

n = sum([int(d) for d in str(int(p) + 1)])

print('Solution to problem 65 is %i.'%n)