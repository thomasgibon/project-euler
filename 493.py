# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:32:39 2015

@author: gibon
"""

from math import factorial
import itertools
from numpy import prod, dot

def C(k,n):
    if k <= n:
        return int(factorial(n)/(factorial(k) * factorial(n-k)))
    return 0

def P(p,n,s):
    """
    Multinomial distribution:
    Probability of getting the sum p with n dice of s faces
    """
    k_max = int((p - n)/s)
    return 1/s**n * sum((-1) ** k * C(n,k) * C(p-s*k-1, n-1) for k in range(k_max + 1))

def allparts(n):
    """ from http://jeromekelleher.net/partitions.php"""
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2*x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

def P_urn(c,colors,colorset,p):
    """
    Probability to get c colors by picking p balls in an urn of colors * colorset balls
    """
    part_list = []
    
    for part in allparts(p):
        if len(part) == c and max(part) <= colorset:
            part_list.extend(set(itertools.permutations(part + [0] * (colors - c))))
    
    P = 0
    
    for part in part_list:
        P += prod([C(k,colorset) for k in part], dtype = 'int64')
    
    return P/C(p,colors * colorset)

n = round(sum([P_urn(k,7,10,20) * k for k in range(0,8)]),10)

print('Solution to problem 493 is %.9f.'%n)