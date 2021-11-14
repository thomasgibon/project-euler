# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:07:16 2015

@author: gibon
"""

import numpy as np

def part(n): # Partitions de n
    p = np.zeros((n,n))
    
    np.fill_diagonal(p,1)
    p[:,0] = np.ones((1,n))
    
    m = 1
    while m < n:
        k = 1
        while k < m:
            p[m, k] = p[m - 1, k - 1] + p[m - k - 1, k]
            k += 1
        m += 1
    return list(map(int,p[-1,:]))

n = int(sum(part(100)[1:]))