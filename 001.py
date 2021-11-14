# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 18:33:09 2015

@author: gibon
"""

# Project Euler - Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
# multiples of 3 or 5 below 1000.

list3 = list(range(3, 1000, 3))
list5 = list(range(5, 1000, 5))

n = sum(set(list3 + list5))

print('Solution to problem 1 is %i.'%n)