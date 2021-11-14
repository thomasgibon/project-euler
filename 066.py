# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:18:48 2015

@author: gibon
"""



ub = 100000

# Technique 4, from http://mathworld.wolfram.com/PellEquation.html

def sqrt_cycle_length(k):
    
    if not isinstance(k, int) or k <= 0:
        raise ValueError("cycle_length(d): d must be a positive integer")
    
    alist = [] # list of remainder
    l = 0
    m = 0
    d = 1
    a = int(k**.5)
    
    a0 = a
    if a0**2 == k:
        return 0, a0, 0
    
    if a0**2 == k - 1:
        return 1, a0, 2*a0
        
    while a:
        m = d * a - m
        d = (k - m**2)/d
        a = int((a0 + m)/d)
        alist.append(a)
        l += 1
        if a == 2 * a0:
            return l, a0, alist
    return 0

def dioph(D):
    r, a0, c = sqrt_cycle_length(D)
    r -= 1
    
    if isinstance(c,int):
        c = [c]
    
    p = [a0, a0 * c[0] + 1]
    q = [1, c[0]]
    
    c = c * 2
    
    for i in range(len(c) - 1):
        a = c[i + 1] # starts at a1
        p.append(a * p[i + 1] + p[i]) # starts at p[2], p2
        q.append(a * q[i + 1] + q[i])
    if r % 2 == 1:
        return p[r],q[r]
    return p[2 * r + 1],q[2 * r + 1]

D_sieve = [True] * ub

for i in range(int(ub**.5)):    
    D_sieve[i*i] = False

D_list = [D for D in range(len(D_sieve)) if D_sieve[D]]

xDmax = [0,0]

for D in D_list:
    x = dioph(D)[0]
    if x > xDmax[0]:
        xDmax = [x,D]

#import numpy as np

# x2 – Dy2 = 1
# x2 = Dy2 + 1

#def divisors(k):
#    divs = []
#    i = 1
#    while i <= int(k**0.5):
#        if k % i == 0:
#            divs.append(i)
#            divs.append(int(k/i))
#        i += 1
#    return sorted(divs)
#
#def factors(k):
#    factors = []
#    i = 2
#    while i <= int(k**0.5):
#        while k%i ==0:
#            factors.append(i)
#            k //= i
#        i += 1
#    if k > 1:
#        factors.append(k)
#    return sorted(factors)

## Technique 1, brute force
###############################
#D_sieve = [True] * ub
#
#for i in range(int(ub**.5)):    
#    D_sieve[i*i] = False
#
#D_list = [D for D in range(len(D_sieve)) if D_sieve[D]]
#x_list = []
#
#for D in D_list[:50]:
#    y = 1
#    x2 = 0
#    notFound = True
#    while notFound:
#        x2 = D * y**2 + 1
#        x = int(x2**.5)
#        if x2 == x**2:
#            x_list.append(x)
#            notFound = False
#            print("%i^2 - %i * %i^2 = 1" % (x,D,y))
#        y += 1

## Technique 2, pick x
################################
#x_list = []
#D_list = []
#y_list = []
#x = 0
#l = 0
#
#while l < 1000:
#    l = len(D_list)
#    if l % 1 == 0 and x > 2:
#        if x == x_list[-1]:
#            print(l, x)
#    x += 1
#    fs = factors(x**2 - 1)
#    sq_fs = [1]
#    D_fs  = []
#    while fs:
#        f = fs.pop()
#        if f in fs:
#            fs.pop(fs.index(f))
#            sq_fs.append(f)
#        else:
#            D_fs.append(f)
#    D = np.prod(D_fs)
##    print(x,D)
#    if D not in D_list and D <= 1000:
#        x_list.append(x)
#        D_list.append(D)
#        y_list.append(np.prod(sq_fs))        
        
# Technique 3, still no success
#x2_with_D_list = []
#D_list = [1]
##y_list = []
##x = 0
#l = 0
#D = 1
#
#x2_list = [x*x for x in range(1,100000)]
#
#while l <= 1000:
##    if l % 100 == 0 and x > 2:
##        print(l, x)
#    for x2 in x2_list:
#        for y2 in x2_list[:x2_list.index(max(x2,int(x2/ub)))]:
#            if (x2 - 1) % y2 == 0:
#                if (x2 - 1)/y2 <= ub:
#                    D = (x2 - 1)/y2
#                    if D not in D_list:
#                        D_list.append(D)
#                        x2_with_D_list.append(x2)
#                        l += 1
#        if x2 % 10000 == 0:
#            print(l,x2**.5,D)
##                if D not in D_list and D <= ub:
##                    l += 1
##                    D_list.append(D)
##                x_list.append(x)
##                y_list.append(y)
#
#
