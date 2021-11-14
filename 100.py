# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:31:41 2015

@author: gibon
"""

"""
Brute force solution: check if 2k(k-1)+1 is square
k is the number of discs, b = (1+sqrt(k))/2 the blue discs
"""

M = 10000

sols = []

for k in range(1,M):
    d = (1 + 2 * k * (k - 1))**.5
    if int(d) == d:
        sols.append((int((1 + d)/2),k))

"""
We can generate all k such that 2k^2-1 is square
https://oeis.org/A001653
"""

def A011900(n):
    return round((((1+2**.5)**(2*n-1) - (1-2**.5)**(2*n-1))/8**.5+1)/2)

def A046090(n):
    return round(1/2 + ((1-2**(1/2))/4)*(3 - 2**(3/2))**(n - 1) +\
                       ((1+2**(1/2))/4)*(3 + 2**(3/2))**(n - 1))

M = 10**12
k = 0

while A046090(k) < M:
    k += 1

n = A011900(k)

print('Solution to problem 100 is %i.'%n)