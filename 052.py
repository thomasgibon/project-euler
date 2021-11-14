# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:47:32 2015

@author: gibon
"""

k = 0
notFound = True

while notFound == True:
    k += 1
    l = len(str(6 * k))
    s = sorted(str(k).zfill(l))
    if sorted(str(2 * k).zfill(l)) == s:
        if sorted(str(3 * k).zfill(l)) == s:
            if sorted(str(4 * k).zfill(l)) == s:
                if sorted(str(5 * k).zfill(l)) == s:
                    if sorted(str(6 * k).zfill(l)) == s:
                        notFound = False

n = k

print('Solution to problem 52 is %i.'%n)