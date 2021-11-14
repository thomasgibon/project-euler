# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:56:56 2015

@author: gibon
"""

import sympy

ub = 10**6
k = 1
tot_ratio_max = 2

while k < ub:
    tot = k / sympy.totient(k)
    if tot > tot_ratio_max:
        tot_ratio_max = tot
        k_max = k
    if k % int(ub/100) == 0:
        print(k,k_max,tot_ratio_max)
    k += 1

n = k_max

print('Solution to problem 69 is %i.'%n)