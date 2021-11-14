# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:51:44 2015

@author: gibon
"""

import numpy as np

data = """21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""

spiral = [[int(num) for num in line.split()] for line in data.splitlines()]

sumdiag0 = sum(np.diag(np.fliplr(spiral))) + sum(np.diag(spiral)) - 1

# at layer (k-1)/2 a diagonal adds up  k^2
#                   + k^2 - (k - 1)
#                   + k^2 - 2 * (k - 1)
#                   + k^2 - 3 * (k - 1)
# = 4 k^2 - 6 * k + 6
#
# for n an odd number
#
# regularizing for n = 2 * k + 1
#
# 1 for k = 0
# 4 * (2*k+1)^2 - 6 * (2*k+1) + 6 for k > 0
#
# calculate 1 + sum(4 * (2*k+1)^2 - 6 * (2*k+1) + 6, k,1,n) + 1) 

def sumdiag(d):
    """Returns the diagonal sums of a dth-degree spiral"""
    return int(1 + (2 * d * (13 + 15 * d + 8 * d ** 2))/3)

# a 1001 * 1001 spiral has degree 500

n = sumdiag(500)

print('Solution to problem 28 is %i.'%n)