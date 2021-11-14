# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:05:29 2015

@author: gibon
"""

import itertools as it

def pythagore_perimeter(p):
    """For a perimeter p, sets of side lengths"""
    
    l = range(1, p)
    
    sets = [comb for comb in it.combinations(l,2) if sum(comb) <= p - 1]
    
    # The problem simplifies to
    # 2000 (a+b) - 2 ab = 1000**2
    
    all_sets = []
    
    for (a,b) in sets:
        if 2. * p * (a+b) - 2. * a * b == p ** 2.:
            all_sets.append(set((a, b, p - a - b)))
    
    return all_sets

if __name__ == "__main__":
    lmax = 0
    for p in range(3,1001):
        print(p)
        l = len(pythagore_perimeter(p))
        if l > lmax:
            lmax, pmax = l, p
        
    n = lmax
    
    print('Solution to problem 39 is %i.'%n)