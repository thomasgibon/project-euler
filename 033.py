# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:31:45 2015

@author: gibon
"""

from fractions import gcd

sols = []

for i in range(10,100):
    for j in range(10,i):
        common = set(str(j)) & set(str(i))
        if common != {'0'} and common != {}:
            for digit in common:
                a = int(str(j).replace(digit,'',1))
                b = int(str(i).replace(digit,'',1))
                if b != 0:
                    if j/i == a/b:
                        sols.append(((j,i),(a,b)))

num = prod([int(frac[1][0]) for frac in sols])
den = prod([int(frac[1][1]) for frac in sols])

n = den/gcd(num,den)

print('Solution to problem 33 is %i.'%n)