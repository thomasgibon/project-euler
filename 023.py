# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:00:29 2015

@author: gibon
"""

def divisors(k):
    divs = []
    i = 1
    while i <= int(k**0.5):
        if k % i == 0:
            divs.append(i)
            divs.append(int(k/i))
        i += 1
    return set(sorted(divs))

def isabundant(k):
    return sum(divisors(k)) - k > k

l = range(2,28124)

ab_list = [k for k in l if isabundant(k)]

s = []

for i in range(len(ab_list)):
    s.extend([ab_list[i] + j for j in ab_list[i:] if ab_list[i] + j <= 28123])

S = set(s)
L = set(range(28124))

s2 = [x for x in L if x not in S]

n = sum(s2)

print('Solution to problem 23 is %i.'%n)