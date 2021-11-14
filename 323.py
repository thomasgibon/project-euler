# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:53:05 2015

@author: gibon
"""

"""
P(X = 0) = 1/2^32
P(X = 1) = ?

N = sum(X*P(X), X = 0..inf)
"""

import numpy as np
from fractions import Fraction

n_list = []
mean_list = []

for k in range(100):
    for l in range(1000):
        y_list = [int(2**32*np.random.random()) for i in range(100)]
    
        x = 0b0
        i = 0
        
        while x < 2**32-1:
            i += 1
            y = y_list[i]
            x = x|y
            
        n_list.append(i)
    
    mean_list.append(np.mean(n_list))


"""
It seems to converge towards 5.35...

Cf. Excel file

The probability for reaching 2^b-1 after n OR operations is
P(N = n) = ((2^n-1)^b-(2^n-2)^b)/(2^(bn))

or


"""

def P_ones(b,n):
    """
    Probability of getting full ones after n OR on b bits
    """
    return Fraction(((2**n-1)**b-(2**n-2)**b)/(2**(b*n)))

# Expectation
E = sum([n*P_ones(32,n) for n in range(100)])

print('Solution to problem 323 is {0}.'.format(E))