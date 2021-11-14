# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 18:43:01 2015

@author: gibon

"""

F = [0,1]
i = 1

while F[i] < 4e6:
    F.append(F[i] + F[i-1])
    i += 1

F = F[:-1]

n = sum([a*b for a,b in zip(F,[j % 2 == 0 for j in F])])

print('Solution to problem 2 is %i.'%n)