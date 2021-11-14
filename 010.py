# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:31:55 2015

@author: gibon
"""

def isprime(k):
    if k == 2:
        return True
    else:
        i = 2
        while i <= int(k**0.5):
            if k % i == 0:
                return False
            i += 1
        return True

i = 1
s = 2

while i < 2e6:
    i += 2
    if isprime(i):
        s += i

n = s

print('Solution to problem 10 is %i.'%n)