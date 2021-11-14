# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:57:24 2015

@author: gibon
"""

"""
We need to generate a list of squarefree numbers. Only them can be radicals.
Multiplying by any existing factor gives a number that has this squarefree as radical.
"""

def sqf_sieve(n):
    l = [True] * n
    for i in range(2,int(n**.5)):
        l[i*i::i*i] = [False] * int((n - 1)/(i*i))
    sqf = [k for k in range(len(l)) if l[k]]
    return sqf

M = 100000

sqf = sqf_sieve(M + 1)[1:]

l = [True] * (M + 1)
for i in sqf_sieve(M + 1)[1:]:
    l[i::i] = [i for k in range(1,int(M/i) + 1)]
    
l = l[1:]

radicals = sorted([(r,k + 1) for k,r in enumerate(l)])

n = radicals[9999][1]

print('Solution to problem 124 is %i.'%n)