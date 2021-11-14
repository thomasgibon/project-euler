# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:32:29 2019

@author: Gibon
"""

def is_pandigital_stepnumber(k):
    strk = str(k)
    # pandigital condition
    if set(int(digit) for digit in strk) == set(range(10)):
           
        #stepnumber condition
        if set(int(strk[i])-int(strk[i-1]) for i in range(1,len(strk))) == {-1,1}:
            return True
        return False
    return False
    
pandigitals = ['0123456789','9876543210']

def pandigital(n):
    
    assert n >= 10
    
    for p in pandigitals:
        start = int(p[0])
        pandigitals.append(str(int(p[0]) + 1))