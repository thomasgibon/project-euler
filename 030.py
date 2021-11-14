# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:29:15 2015

@author: gibon
"""

import matplotlib.pyplot as plt

fi = []
sols = []

for i in range(2,300000):
    f = [int(j)**5 for j in str(i)]
    fi.append(sum(f))
    if i == sum(f):
        sols.append(i)
        print(i)


# check upper bound is correct with
plt.plot(fi),plt.plot(range(300000))

n = sum(sols)

print('Solution to problem 30 is %i.'%n)