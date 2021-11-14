# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:55:17 2015

@author: gibon
"""

import numpy as np

n = np.array([int(k) for k in list(str(2**1000))]).sum()

print('Solution to problem 16 is %i.'%n)