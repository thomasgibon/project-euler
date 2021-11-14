# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:21:53 2015

@author: gibon
"""


s_list = []
ub = 10000

for i in range(ub):
    s = ''
    l = 0
    j = 1
    while l <= 9:
        t = set(str(i * j))
        li = len(str(i * j))
        l += li
        if t & set(s) == set() and len(t) == li and '0' not in t:
            s += str(i * j)
            j += 1
        else:
            pass
    if len(s) == 9:
        s_list.append((i,j - 1,s))

n = max([int(s[2]) for s in s_list])

print('Solution to problem 38 is %i.'%n)