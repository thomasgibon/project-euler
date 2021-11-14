# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:04:09 2015

@author: gibon
"""

n = 600851475143
i = 2

while i**2 < n:
    while n % i == 0:
        n = n / i
    i += 1

print('Solution to problem 3 is %i.'%n)