# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:02:49 2015

@author: gibon
"""

from math import factorial as fact

def C(n,r): # Combinations
    if n < 0 or r < 0 or n < r:
        return 0
    if isinstance(r,int) and isinstance(n,int):
        return int(fact(n)/(fact(r)*fact(n-r)))

def P(p,n,s):
    """
    Probability of getting the sum p with n dice of s faces
    """
    k_max = int((p - n)/s)
    return 1/s**n * sum((-1) ** k * C(n,k) * C(p-s*k-1, n-1) for k in range(k_max + 1))