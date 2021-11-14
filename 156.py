# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:16:14 2016

@author: gibon
"""

import math

def f_brute(n,d):
    c = 0 # counter
    c_list = []
    sols = []
    for m in range(n + 1):
        c += str(m).count(str(d))
        c_list.append(c)
        if m == c:
            sols.append(m)
    return c, c_list, sols

'''
m = sum a_i * 10**i

e.g. 23
there's been 10 times 1 in first
there's been (2+1) times 1 in second

e.g. 23423

first digit: 2
- there's been 10000 ones in first position,
second digit: 3
- there's been (2+1)*min(3423-1000,1000) ones in second
third digit: 4
- there's been (23+1)*min(423-100,100)
forth digit: 2
- there's been (234+1)*min(23-10,10)
fifth digit: 3
- there's been (2342+1)*max(min(3-1,1),0)

if d = 2

e.g. 245

first digit: 2
- there's been 0 * 100 twos in first position
second digit: 4
- there's been 
'''

def f(n,d):
    
    N = str(n)
    
    l = len(N) # maximum power of 10 in decimal decomp.
    c = 0
    
    for p, D in enumerate(N): # position, digit
        m = n//10**(l - p)
        print(m)
        
        c += (m + (int(D) > d) * 1) * 10**(l - p - 1)
    
    return c