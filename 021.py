# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:20:36 2015

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

# Upper bound
ub = 10000

# List of sum of divisors
div = [sum(divisors(i)) - i for i in range(ub+1)]
div_test = [sum(divisors(i)) - i for i in range(max(div)+1)] # we create this list to handle potential amicable pairs with one number > 10000

# extract amicables and check they all appear
amic = [(i,j) for i,j in enumerate(div) if div_test[j] == i]

n = sum(set([i[0] for i in amic if i[0] != i[1]]))

print('Solution to problem 21 is %i.'%n)