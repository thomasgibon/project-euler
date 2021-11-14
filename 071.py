# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:41:36 2015

@author: gibon
"""

import sympy

def listfrac(N):
    l = []
    for d in range(1,N + 1):
        for n in range(1,d):
            l.append(sympy.nsimplify(n/d))
    return sorted(list(set(l)))

test = [(i,listfrac(i)[listfrac(i).index(3/7) - 1]) for i in range(8,30)]

# We see that the numerators are of the form 3 * k - 1
# and the denominators are of the form       7 * k - 2
# for the range [7 * k - 2 : 7 * k + 4]

# Find the first integer in the range where 1000000 belongs

k_list = [int((i + 2) / 7) for i in range(30)]
d_list = [7 * k - 2 for k in k_list]
n_list = [3 * k - 1 for k in k_list]
f_list = [sympy.nsimplify(n/d) for n,d in zip(n_list,d_list)]

n = 3 * int((10**6 + 2) / 7) - 1

