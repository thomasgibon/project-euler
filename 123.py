# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:08:16 2015

@author: gibon
"""

from sympy import prime
"""
def remainder(n):
    if n%2 == 0:
        return 2
    p = prime(n)
    r = ((p-1)**n + (p+1)**n) % (p*p)
    # q = int(((p-1)**n + (p+1)**n)/(p*p))
    return r#,q
    
    
(p - 1)**n + (p + 1)**n % p^2 is:
- 2 when n is even,
- 2*n*pn % when n is even
"""

def remainder(n):
    if n%2 == 0:
        return 2
    p = prime(n)
    return (2*n*p) % (p*p)
    
sols = [(0,0,0)]

for e in range(1,12):

    r = 0
    n = 1

    while r < 10**e:
        n += 2
        r = remainder(n)

    sols.append((e,n,r))

n = sols[10][1]

print('Solution to problem 123 is %i.'%n)