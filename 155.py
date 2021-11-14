# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:11:23 2015

@author: gibon
"""

from numpy import prod
from sympy import totient, sieve
from fractions import Fraction

def R(n):
    return Fraction(totient(n),(n-1))

k = 1

def capacities(k):
    if k == 1:
        return 1
    return 2 * sum(totient(k) for k in range(1,k+1)) - 1