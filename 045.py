# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:27:38 2015

@author: gibon
"""

def is_tri(k):
    t = (- 1 + (1 + 8 * k)**.5) / 2
    if t == int(t):
        return int(t)
    else:
        return False

def is_pen(k):
    p = (1 + (1 + 24 * k)**.5) / 6
    if p == int(p):
        return int(p)
    else:
        return False

def is_hex(k):
    h = (1 + (1 + 8 * k)**.5) / 4
    if h == int(h):
        return int(h)
    else:
        return False

lb = 40755
notfound = True
p = int((1+24*lb)**.5)

while notfound:
    p += 1
    k = int((p**2 - 1)/24) # it cannot be a pentagonal otherwise
    if p % 1000 == 0:
        print(k)
    if is_tri(k):
        if is_pen(k):
            print(k)
            if is_hex(k):
                n = k
                n_list = (k,is_tri(k),is_pen(k),is_hex(k))
                print(n_list)
                notfound = False

print('Solution to problem 45 is %d.'%n)