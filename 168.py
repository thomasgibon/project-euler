# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:07:42 2016

@author: gibon
"""

KMAX = 6

def rightrotate(i):
    return int(str(i)[-1] + str(i)[:-1])

valid_numbers = (i for i in range(int(10**(KMAX-1)),int(10**KMAX)) if int(str(i)[-1]) >= 2*int(str(i)[0]))

sols = []

##for i in a:
for i in valid_numbers:
    j = rightrotate(i)
    if j % i == 0 and len(set(str(i))) > 1: 
        divisor = j//i
        print(j, i, divisor)
        sols.append(j)
#        
#for i in range(10**14,2*10**14):
#    if rightrotate(i) % i == 0:
#        print(rightrotate(i), i, rightrotate(i)//i)
#        sols.append(rightrotate(i))
#
#
#for i in range(100000,999999):
#    divisor = rightrotate(i)/i
#    if abs(round(divisor) - divisor) < .0001 and len(set(str(i))) > 1:
#        print(rightrotate(i), i, divisor)

def parasitic(n,k,limit=100):
    
    assert n < 10 and k < 10
    
    if k < n:
        print('k < n, no solution')
        return [0]
    c = 0
    k_0 = k
    
    while n*k != rightrotate(k):
        
        c += 1
        k = int(str(n*k)[-c:] + str(k_0))

        if len(str(k)) > limit:
            print('no number strictly under digit limit of {}'.format(limit))
            return [0]
    
    all_results = [int(str(k) * (i+1)) for i in range(int(limit/len(str(k))))]
    
    return(all_results)

solutions = sorted([p for n in range(1,10) for k in range(1,10) for p in parasitic(n,k,limit=100) if p>10])

n = sum(solutions)