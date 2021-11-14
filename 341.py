# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:44:47 2016

@author: gibon
"""

import numpy as np

def G_old(n):
    
    g_list = [1]
    d_list = [0]
    
    if n == 1:
        return 1

    G = 1

    for i in range(2,n):
        if sum(g == g_list[i-2] for g in g_list) == g_list[g_list[i-2]-1]:
            G += 1
            d_list.append(i)
        g_list.append(G)
        
    return g_list, d_list

'''
From https://oeis.org/A001462
a(1) = 1; a(n+1) = 1 + a(n+1-a(a(n)))
'''

def G(n):
    
    g_list = [1]    
    
    for i in range(2,n):
        g_list.append(1 + g_list[i - 1 - g_list[g_list[i - 2] - 1]])
    
    return g_list

def G_sieve(n):
    
    g_sieve = [0, 1, 2, 2]
    
    i = 3    
    
    while i < n:
        g_sieve.extend(g_sieve[i] * [i])
        i += 1
    
    return g_sieve
    