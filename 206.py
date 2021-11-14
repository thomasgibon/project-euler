# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:10:40 2015

@author: gibon
"""

import numpy as np
from fractions import gcd
from sympy import factorint

# Find k integer for k**2 = s, where '_' is a single digit in s
# For a square to end in 9_0, k must end in 30 or 70

s = '1_2_3_4_5_6_7_8_9_0'
#test_pattern = zip(range(0,19,2),'1234567890')

k_min = int(int(s.replace('_','0'))**.5)
k_max = int(int(s.replace('_','9'))**.5)

k_list = (k for k in range(k_min,k_max) if str(k)[-1] == 0)

test30 = [(k,k*k) for k in range(1010101030,k_max,100) if np.prod([str(k*k)[i] == j for i,j in zip(range(-15,0,2),'1234567890')])]
test70 = [(k,k*k) for k in range(1010101070,k_max,100) if np.prod([str(k*k)[i] == j for i,j in zip(range(-15,0,2),'1234567890')])]

for k in range(1010101030,k_max,100):
    if k%1e6 == 30:
        print(k)
    if all([str(k*k)[i] == j for i,j in zip(range(0,19,2),'1234567890')]):
        print(k,k*k)


for k in range(1010101070,k_max,100):
    if k%1e6 == 70:
        print(k)
    if all([str(k*k)[i] == j for i,j in zip(range(0,19,2),'1234567890')]):
        n = k*k
        print(k,k*k)