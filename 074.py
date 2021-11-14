# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:01:04 2015

@author: gibon
"""

from math import factorial
from itertools import combinations_with_replacement, permutations
from string import digits

def sumfact(k):
    if isinstance(k, int):
        return sum([factorial(int(i)) for i in str(k)])
    return False

def factchain(N):
    k0 = N
    k  = sumfact(k0)
    i  = 1
    k_list = [k0]
    
    while k not in k_list:
        k_list.append(k)        
        k = sumfact(k)
        i += 1
    return k_list

if __name__ == "__main__":
    ub = 10**6
    maximum = 9*factorial(9)
    
    chain_len = [False] * maximum
    
    for k in range(ub + 1):
        if k % 10000 == 0:
            print(k)
        if not chain_len[k]:
            k_chain = factchain(k)
            for i in k_chain:
                if not chain_len[i]:
                    chain_len[i] = len(k_chain) - k_chain.index(i)
#            k_chain = [k]
#            k = sumfact(k)
#            while not k in k_chain:
#                if k <= ub and not chain_len[k]:
#                    k_chain.append(k)
#                    k = sumfact(k)
#            for i in k_chain:
#                chain_len[i] = len(k_chain) - k_chain.index(i) + chain_len[k]

n = sum([l == 60 for l in chain_len])

# Alternative solution, only testing one combination of numbers
def digit_factorial(n):
    return str(sum(map(factorial,map(int,n))))

chains = set()
for r in range(1,7):
    for x in combinations_with_replacement(reversed(digits),r):
        n = ''.join(x)
        chain = [n]
        next_in_chain = digit_factorial(n)
        while next_in_chain not in chain:
            chain.append(next_in_chain)
            next_in_chain = digit_factorial(next_in_chain)
        if len(chain)==60:
            chains.add(n)
total = 0
for n in chains:
    d = digit_factorial(n)
    total += sum(digit_factorial(str(int(k))) == d for k in {''.join(x) for x in permutations(str(n))})
print(total)