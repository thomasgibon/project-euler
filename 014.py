# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:36:31 2015

@author: gibon
"""

def syracuse(n):
    '''
    Syracuse chain for number n
    '''
    chain = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
            chain.append(int(n))
        else:
            n = 3 * n + 1
            chain.append(int(n))
    return chain

chain_length = []

for i in range(1000000):
    chain_length.append(len(syracuse(i)))

n = chain_length.index(max(chain_length))

print('Solution to problem 14 is %i (chain of %i elements).'%(n,max(chain_length)))