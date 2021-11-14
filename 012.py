# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:19:49 2015

@author: gibon
"""

def divisors(k):
    divs = []
    i = 1
    while i <= int(k**0.5):
        if k % i == 0:
            divs.append(i)
            divs.append(int(k/i))
        i += 1
    return set(sorted(divs))

k = 0
divs = []

while len(divs) <= 500:
    t = k * (k+1) / 2 # kth triangle number
    divs = divisors(t)
    k += 1

n = t

print('Solution to problem 12 is %i.'%n)