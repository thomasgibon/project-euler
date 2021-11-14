# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:33:47 2019

@author: Gibon
"""

'''
Conjecture: geometric sums start with the smallest number possible, with the reason q being as close to one as possible.

i.e. the smallest u0 for q = k+1/k with highest k
'''


from sympy.ntheory import factorint, divisors, composite
from sympy.ntheory.factor_ import core, perfect_power

import numpy as np 

def maximum_geo_sum(m):
    solution = ()
    for k in range(1,10):
        
        q = (k+1)/k
        s_max = 0
            
        S = [m]
        next_m = m/q
        
        while next_m == int(next_m):
            next_m = int(next_m)
            S.append(next_m)
            next_m /= q
            
        if len(S)<3:
            S = []
        
        if sum(S) > s_max:
            
            s_max = sum(S)
            solution = (S,s_max,(int(next_m*q),k))
    
    if not solution:
        solution = maximum_geo_sum(m-1)
            
    return solution

all_solutions = []


def maximum_geo_sum_all(max_m):
    
    all_solutions = []
    s_max = 0
    
    for m in range(4, max_m+1):
            
        solution = ()
        for k in range(1,100):
            
            q = (k+1)/k
        
            S = [m]
            next_m = m/q
            
            while next_m == int(next_m):
                next_m = int(next_m)
                S.append(next_m)
                next_m /= q
                
            if len(S)<3:
                S = []
            
            if sum(S) > s_max:
                
                s_max = sum(S)
                solution = (S,s_max,(int(next_m*q),k))
                all_solutions.append((m,solution))
                    
        if not solution:
            all_solutions.append((m,all_solutions[-1][1]))
                
    return all_solutions

def max_geo_sum_all2(p):
    '''
    Now the strategy for p is to find its highest divisor d with order n >= 2,
    and multiply it by (d-1)/d = 1-1/d n times to get the terms
    
    the sum is p * d * (1 - (1 - 1/d)**(n+1))
    
    /!\ d should be the root of the highest perfect power
    
    e.g.
    10 = 2*5 -> does not have highest dividing power, takes 9's 3**2 -> S = 9*3*(1-(1-1/3)**3) = 19
    72 = 2**3*3**2 -> highest dividing power is 6**2 -> S = 72*6*(1-(1-1/6)**3) = 182
    121500 = 2**2*3**5*5**3 -> highest dividing power is 15**3 (NB: not 30**2!), etc.
    '''
    all_solutions = []
    s_max = 0
    
    for m in range(4,p+1):
        
        if m%10000==0:
            print(m)

        perfect_power_divisors = []
        
        for d in divisors(m, generator=True):
            
            fs = set(factorint(d).values())
            
            if fs != {1} and len(fs) == 1:
                
                perfect_power_divisors.append(d)
        
        if perfect_power_divisors:
            
            d,o = perfect_power(max(perfect_power_divisors), big=True)
            s = round(m*d*(1-(1-1/d)**(o+1)))
            
            if s>s_max:
                s_max = s
                all_solutions.append((m, s_max))

    return all_solutions        

test = [(m[0],
         (-1)**m[0]*m[1]) for i,m in enumerate(max_geo_sum_all2(1000))]