# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:46:52 2015

@author: gibon
"""

import numpy as np

# k parmi n = n!/(k!(n-k)!)
k = 20
n = 40
c = np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k))

n = c

print('Solution to problem 15 is %i.'%n)