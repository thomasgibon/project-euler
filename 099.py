# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:15:32 2015

@author: gibon
"""

import urllib
from sympy import ln

file_url = 'https://projecteuler.net/project/resources/p099_base_exp.txt'
k_list   = [[int(k) for k in row.split(',')] + [row_nb + 1] for row_nb, row in
enumerate(urllib.request.urlopen(file_url).read().decode('utf-8').split())]

n     = 0
i_max = 0

for k,p,nb in k_list:
    i = p * ln(k)
    if i > i_max:
        i_max = i
        n = nb

print('Solution to problem 18 is %i.'%n)