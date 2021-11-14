# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:22:17 2015

@author: gibon
"""

# S(n,2) = n(n+1)(n+2)/6

def sumsq(n):
    return n*(n+1)*(2*n+1)/6

def sqsum(n):
    return n**2*(n+1)**2/4

n = sqsum(100) - sumsq(100)

print('Solution to problem 6 is %i.'%n)