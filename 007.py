# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:28:55 2015

@author: gibon
"""

def isprime(k):
    if k <= 1:
        return False
    if k == 2:
        return True
    else:
        i = 2
        while i <= int(k**0.5):
            if k % i == 0:
                return False
            i += 1
        return True

c = 1
i = 1

while c <= 10001:
    i += 1
    if isprime(i):
        c += 1

n = i

print('Solution to problem 7 is %i.'%n)