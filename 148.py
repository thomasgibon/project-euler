# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:06:02 2015

@author: gibon
"""

# Find the number of entries which are not divisible by 7 in the first one
# billion (10^9) rows of Pascal's triangle.

from mpmath import mp
import matplotlib.pyplot as plt
import numpy as np

mp.dps = 50

def pascals_triangle(n_rows):
    results = [] # a container to collect the rows
    for _ in range(n_rows): 
        row = [1] # a starter 1 in the row
        if results: # then we're in the second row or beyond
            last_row = results[-1] # reference the previous row
            # this is the complicated part, it relies on the fact that zip
            # stops at the shortest iterable, so for the second row, we have
            # nothing in this list comprension, but the third row sums 1 and 1
            # and the fourth row sums in pairs. It's a sliding window.
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # finally append the final 1 to the outside
            row.append(1)
        results.append(row) # add the row to the results.
    return results

n_rows = 49

k = 7

div7 = np.array([[(p%k == 0) * 1 for p in row] + [-1] * (n_rows - len(row)) for row in pascals_triangle(n_rows)])
plt.pcolor(div7)
plt.gca().invert_yaxis()

# the amount of non-7-divisible numbers for a triangle of side 14
# is 28 * 3
# their proportion is 28 * 3 / (28 * 3 + 21) = 4/5

# the amount of non-7-divisible numbers for a triangle of side 49
# is 28**2
# their proportion is 28**2 / (28**2 + 21**2) = 4/5

s = []

for i in range(1001):
    s.append(sum([sum([p%7 != 0 for p in row]) for row in pascals_triangle(i)]))

plt.plot(s)

p = mp.mpf(1/(1 + (k - 1)/(k + 1) * 3/4))

# number of values
n = p * mp.mpf(7 * k * (7 * k + 1)/2)