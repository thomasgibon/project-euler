# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:56:37 2015

@author: gibon
"""

import numpy as np

# LENT
def part(n): # Partitions de n
            
    p = np.zeros((n,n))
    
    np.fill_diagonal(p,1)
    p[:,0] = np.ones((1,n))
    
    m = 1
    while m < n:
        i = 1
        while i < m:
            p[m, i] = p[m - 1, i - 1] + p[m - i - 1, i]
            i += 1
        m += 1
    return p

# RAPIDE
def part_pent(n):

    p_list = [0,1]
    
    max_pent_pos = int((1+(1+24*n)**.5)/6)
    max_pent_neg = int((1-(1+24*n)**.5)/6)
    pents = sorted([(int(k*(3*k-1)/2),k) for k in range(max_pent_neg,max_pent_pos + 1)])[1:]
    
    for i in range(2,n+2):
        p = sum([(-1)**(k + 1) * p_list[i - pent] for pent, k in pents if pent <= i])
        p_list.append(int(p))
        
    return p_list

p_list = [1,1]
m = 2

# ITERATIF
while p_list[-1] != 0:
    
    max_pent_pos = int((1+(1+24*m)**.5)/6)
    max_pent_neg = int((1-(1+24*m)**.5)/6)
    pents = sorted([(int(k*(3*k-1)/2),k) for k in range(max_pent_neg,max_pent_pos + 1)])[1:]
    
    p = sum([(-1)**(k + 1) * p_list[m - pent] for pent, k in pents if pent <= m])
    p_list.append(int(p) % 10**6)
    
    if m % 1000 == 0:
        print(m,p_list[-1])
        
    m += 1

n = m - 1

print('Solution to problem 78 is %i.'%n)