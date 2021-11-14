# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:30:36 2015

@author: gibon
"""

import re
import string
import numpy as np

f = open('p022_names.txt','r')
l = [line for line in f.readlines()]

names = re.split('","|"',l[0])
names = sorted([w for w in names if w != ''])

alph = string.ascii_uppercase

name_value = [sum([alph.index(letter) + 1 for letter in name]) for name in names]

n = np.dot(range(1, len(names) + 1), name_value)

print('Solution to problem 22 is %i.'%n)