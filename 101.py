# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:38:22 2015

@author: gibon
"""

import numpy as np

P = np.polynomial.Polynomial([1,-1,1,-1,1,-1,1,-1,1,-1,1])
d = P.degree()
x_s = range(1,d + 1)

A = np.array([[x**j for j in range(d - 1,-1,-1)] for x in x_s])
b = P(x_s)

s = 0

for x in x_s:
    coefs = np.linalg.solve(A[:x,d-x:],b[:x])[::-1]
    OP = np.polynomial.Polynomial(coefs)
    
    s += round(OP(x + 1))

n = int(s)

print('Solution to problem 101 is %i.'%n)