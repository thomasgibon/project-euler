# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 18:08:41 2016

@author: gibon
"""

import math
from sympy import factorint, gcd

def M_exact(N):
    result = max([((N/k)**k,k) for k in range(1,N)])
    return result

'''
d/dk ((n/k)**k)

d/dk (k*log(n/k)) = k*(log(n) - log(k))
                  = log(n) - log(k) * k*(-1/k)
                  = - 1 + log(n) - log(k)
                  
- 1 + log(n) - log(k) = 0

log(k) = log(n) - 1
-> k = n / e

and maximum is:
(n/(n/e))**(n/e)

e**(n/e) = (e**(1/e))**n
'''

def M(N):
    if N in [1,2]:
        return (N,1)
    k = round(N/math.e)
    return k,(N/k)**k

def D(N):
    # first reduce the fraction
    m = M(N)[0]
    g = gcd(N,m)   
    b = m/g
    
    # now only if b is 1 or a multiple of 2 and/or 5 the fraction terminates
    f = set(factorint(b).keys())
    
    if f < {2,5}:
        return -N
        
    return N