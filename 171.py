# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:31:16 2019

@author: Gibon
"""

def f(p):
    assert type(p) == int
    return sum(int(digit)**2 for digit in str(p))