# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:32:14 2015

@author: gibon
"""

# Following https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

def sqrt_digit(n,k):
    
    if int(n**.5) ** 2 == n:
        return [n]
        
    d_list = []
    n_str = len(str(n))%2 * '0' + str(n)
    groups = [int(n_str[i:i+2]) for i in range(0, len(n_str), 2)]
    groups.extend([00] * k)
    p, x, y, c = (0, 0, 0, 0)
    
    for g in groups:
        c = 100 * c + g
        x = 0
        while x * (20 * p + x) < c:
            x += 1
        x -= 1
        y = x * (20 * p + x)
        d_list.append(x)
        c -= y
        p = 10 * p + x
        
    return d_list

n = sum([sum(sqrt_digit(i,99)) for i in range(101) if int(i**.5) ** 2 != i])