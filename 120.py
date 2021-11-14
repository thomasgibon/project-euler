# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:23:26 2016

@author: gibon
"""

def r(a,n):
    return ((a-1)**n+(a+1)**n) % a**2
    
def r_max(a):
    if a % 2 == 1: # If a odd
        return a * (a - 1), int((a - 1)/2)
    elif a % 2 == 0:
        return a * (a - 2), int((a - 2)/2)
    else:
        raise ValueError('The argument is not a integer')

'''
A bit of calculus

for n even, r = 2
for n odd,
r = 2*binomial(n,n-1)*a mod a2

binomial(n,n-1) = n
2*n*a mod a2 = (2*n mod a) * a

=> r = (2*n mod a) * a

r_max is found for (2*n mod a)_max

=> n_max = (a-1)/2
   r_max = (a-1)*a

sum(n*(n-1),3,1000) = [n*(n+1)*(2*n+1)/6 - n*(n+1)/2]_3^1000

s = [n*(n+1)*(2*n-2)/6] _3 ^1000
'''

#s = (1000*1001*1998 - 2*3*2)/6

def r_max(a):
    
    r_max = 0
    n_max = 0
    
    for n in range(1,2*a,2):
        
        r = ((a-1)**n+(a+1)**n)%(a**2)
        
        if r > r_max:
            r_max = r
            n_max = n
            
    return n_max, r_max

sum(r_max(a)[1] for a in range(3,1001))
