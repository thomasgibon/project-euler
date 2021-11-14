# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:04:11 2015

@author: gibon
"""

# Making all palindroms < 1000000
pal_even = [int(str(i) + str(i)[::-1]) for i in range(1000)]
pal_odd  = [int(str(i) + str(i)[-2::-1]) for i in range(1,1000)]

palindroms = sorted(pal_even + pal_odd)

pal_bin_dec = [i for i in palindroms if bin(i)[2:] == bin(i)[:1:-1]]

n = sum(pal_bin_dec)

print('Solution to problem 36 is %i.'%(n))