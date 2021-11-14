# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:33:45 2016

@author: gibon
"""

import numpy as np

def f(i):
    if i == 1:
        return 1
    elif i == 3:
        return 3
    elif i%2 == 0:
        return f(i/2)
    elif i%4 == 1:
        return 2*f((i-1)/2+1)-f((i-1)/4)
    elif i%4 == 3:
        return 3*f((i-3)/2+1)-2*f((i-3)/4)

def S(n):
    return sum(f(i) for i in range(1,n+1))

f_list = np.array([[0,0],[1,0],[1,0],[0,1]])

for i in range(4,1001):
    if i%2 == 0:
        f_list = np.vstack([f_list,f_list[int(i/2)]])
    elif i%4 == 1:
        f_list = np.vstack([f_list,2*f_list[int((i-1)/2+1)]-f_list[int((i-1)/4)]])
    elif i%4 == 3:
        f_list = np.vstack([f_list,3*f_list[int((i-3)/2+1)]-2*f_list[int((i-3)/4)]])

"""
For odd numbers, the nth term of f is:
3*a(n) - 1*(a(n) - 1) = 2*a(n) + 1
with a(n) being 1zy...ba with n = 1ab...yz in binary
"""

def f2(n):
    if n%2 == 0:
        return f2(int(n/2))
    k = int((n-1)/2)
    return 2*int(bin(k)[:3]+bin(k)[:2:-1],2)+1

def S2(n):
    return sum(f2(i) for i in range(1,n+1))

"""
Actually f just reverses the binary notation!
"""

def f3(i):
    return int(bin(i)[:1:-1])

"""
At the end of each complete cycle n (3, 7, 15, 31... 2^n - 1) the sum of:
+ even terms is (4^n - 1)/3
+ odd terms is 4^n
= (4^n - 1)/3

If k = 2^n - 1, then
S(k) = (4^n - 1)/3
"""
