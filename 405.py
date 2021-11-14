# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:20:54 2021

@author: Gibon
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sympy import symbols, solve, roots, solve_poly_system

T0 = np.array([(0,0),(0,1),(2,0),(2,1)])
tr = [[0,1],[1,0]]


def transform(T:np.array, n:int):
    
    if n==0:
        return T, {1: 4}
    
    tr = [[0,1],[1,0]]
    # else:
    #     T_next = np.concatenate((T.dot(tr),
    #                     T.dot(tr) + [3,0],
    #                     T + [1,0],
    #                     T + [1,1]))/2
    
    T_next = np.concatenate((T.dot(tr),
                    T.dot(tr) + [3,0],
                    T + [1,0],
                    T + [1,1]))/2
    
    if n>1:
        return transform(T_next, n-1)
    
    count = Counter(tuple(tuple(x) for x in T_next))
    
    return T_next, count

def plotT(n):
    
    T,count=transform(T0, n)
    
    x,y=zip(*T)
    
    c=['b' if v<4 else 'r' for v in [count[tuple(k)] for k in T]]
    
    plt.scatter(x,y,s=.05,c=c)

A=np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[8,-6,-7,6]])
c=np.array([0,0,2,16])

def countf(n, c:np.array, A:np.array):
    
    if n==0:
        return c
    c=A.dot(c)%410338673
    if n>1:
        return countf(n-1,c,A)
    
    return c


def fastpower(i,n,mod=410338673):
# this looks broken
    while n>1:
        sq=(i*i)%mod
        if n%2==0:
            i=sq
            n/=2
        else:
            i=i*sq
            n=(n-1)/2
    return i%mod

def fpower(i,n,mod=410338673):
    if n==1:
        return i%mod
    elif n%2==0:
        return fpower(i*i,n//2)%mod
    else:
        return i*fpower(i*i,(n-1)//2)%mod

# T=T0
# for n in range(11):
#     T = np.concatenate((T.dot(tr),
#                 T.dot(tr) + [3,0],
#                 T + [1,0],
#                 T + [1,1]))/2
#     c_n = Counter(tuple(tuple(x) for x in T))
#     print((n,Counter(c_n.values())[4]))

# Use eigenvalues
D,V=np.linalg.eig(A.astype(np.float64))
Vi=np.linalg.inv(V)
Dd=np.diag(D)

# A**100=V@Dd**100@Vi

# D=[ 4., -1.,  2.,  1.] so we need to find the 10**9 power of 4 and 2
# raising to 1e9th power takes 29 squarings

F=[0,0,2,16]
def A_power(n):
    
    D = [fastpower(4,n), (-1)**(n%2), fastpower(2,n), 1]
    A_p = V@np.diag(D)@Vi
    
    return A_p

#%% The polynomial way

x = symbols('x')

# Closed form of the recurrence is sum(a_i*lambda_i**n)
# with lambdas the eigenvalues
# also the roots of the characteristic polynomial
rs = solve(x**4 - 6*x**3 + 7*x**2 + 6*x - 8, x)
S = np.vstack([np.power(rs,i).astype(int) for i in range(4)])

# Solving for initial conditions we get the a_i
a_i = np.linalg.solve(S,[0,0,2,16])

# This is numerical but quite transparent:
a_i = np.array([-1/15, 1, -4/3, 2/5])

def roots_power(n):
    return [(-1)**n, 1, fpower(2,n), fpower(4,n)]

def f_n(n):
    if n==0:
        return 0
    return ((15*a_i).dot(roots_power(n))%410338673)/15