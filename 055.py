# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 00:52:35 2015

@author: gibon
"""

def lychrel(k, depth = 50):
    k += int(str(k)[::-1])
    i = 1
    while str(k) != str(k)[::-1] and i < depth:
        k += int(str(k)[::-1])
        i += 1
    if i == depth:
        return False
    else:
        return i, k

n = sum(lychrel(i) == False for i in range(10000))

print('Solution to problem 55 is %i.'%n)