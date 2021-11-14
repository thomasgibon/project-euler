# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:01:25 2015

@author: gibon
"""

import numpy as np

f = np.math.factorial(100)
n = sum([int(k) for k in str(f)])

print('Solution to problem 20 is %i.'%n)