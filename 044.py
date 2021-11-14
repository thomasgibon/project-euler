# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:36:43 2015

@author: gibon
"""

def pent(k):
    """kth pentagonal number"""
    return int(k * (3 * k - 1) / 2)

pents = [pent(i) for i in range(1,3000)]

exitFlag = False


for pi in pents:
    if exitFlag:
        break
    for pj in pents[:pents.index(pi)]:
        if pi + pj in pents:
            print((pents.index(pi),pents.index(pj)))
        if pi + pj in pents and pi - pj in pents:
            D = abs(pi - pj)
            exitFlag = True

n = D

print('Solution to problem 44 is %i.'%n)