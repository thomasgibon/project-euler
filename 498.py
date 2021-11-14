# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:08:12 2020

@author: Gibon



For positive integers n and m, we define two polynomials Fn(x) = xn and Gm(x) = (x-1)m.
We also define a polynomial Rn,m(x) as the remainder of the division of Fn(x) by Gm(x).
For example, R6,3(x) = 15x2 - 24x + 10.

Let C(n, m, d) be the absolute value of the coefficient of the d-th degree term of Rn,m(x).
We can verify that C(6, 3, 1) = 24 and C(100, 10, 4) = 227197811615775.

Find C(1013, 1012, 104) mod 999999937.

Fn(x) = An-m(x)Gm(x) + Rn,m(x)

some tests

>>> eq = x**6 - (x**3 + 3*x**2 + 6*x + 10)*(x-1)**3
>>> simplify(eq)
15x2−24x+10

>>> eq = x**7 - (x**3 + 3*x**2 + 6*x + 10)*(x-1)**4
>>> simplify(eq)
x6+15x3−39x2+34x−10

"""

from sympy import *
import numpy as np
import scipy.linalg

def fact(k):
    if k in [0,1]:
        return 1
    return k*fact(k-1)

def binomial_coefs_r(degree):
    if degree == 0:
        return np.array([1])
    return np.hstack([[0],binomial_coefs_r(degree-1)]) + np.hstack([binomial_coefs_r(degree-1),[0]])

def binomial_coefs_signed(degree, padding=0):
    coefs = []
    for d in range(degree+1):
        coefs.append((-1)**(d)*int(fact(degree)/(fact(degree-d)*fact(d))))
    return np.array(coefs+[0]*padding)

B = np.matrix([[1,0,0,0],[-3,1,0,0],[3,-3,1,0],[-1,3,-3,1],[0,-1,3,-3],[0,0,0-1,3],[0,0,0,-1]])

np.linalg.solve(B[:4,:],[1,0,0,0])
# array([  1.,   3.,   6.,  10.])
# sum of integers...

n = 6
m = 3

# rank of A matrix is 4
r = n - m + 1


#[int(k*(k+1)/2) for k in range(1,r+1)]
# OK there's a function for that...
def R_alg(n,m):
    r = n - m + 1
    a = np.cumsum(range(1,r+1))
    B = scipy.linalg.toeplitz(binomial_coefs_signed(m,padding=n-m), [1]+[0]*(n-m))[r:,:]
    return -B.dot(a)

#def R(n,m):
#    x = Symbol('x')
#    eq = x**n - Poly(np.cumsum(range(1,n-m+2)),x)*(x-1)**m
#    return eq.coeffs()
    
def R(n,m):
    # coefficients of quotient times Gm(x)
#    qg = np.outer([fact(k)/(fact(m-1)*fact(k-m+1)) for k in range(n-m,n)], binomial_coefs_signed(m)[:-1]).T
    qg = np.outer([binomial(k,m-1) for k in range(n-m,n)],
                   binomial_coefs_signed(m)[:-1]).T
#    print(qg)
    return [qg.trace(i) for i in range(m)]

# C(n,m,0) is always the sum of a single term, binomial(n-1,m-1)
def C(n,m,d):
    
    c = 0
    
    for k in range(d+1):

        cc = binomial(m,k) * binomial(n-d-1+k, m-1) * (-1)**(d-k)
#        print(k,m,m-1,n-d-1+k,cc)
        c += cc
    return c 

C(100,10,4)
# can also be written 95*94*93*92*91*90*89*88*87/fact(9)*(1+10*96/87*(-1+9/2*97/88*(1+8/3*98/89*(-1+7/4*99/90))))

def C_r(n,m,d):
    
    c = 0
    
    while d > 0:
#        print((m-d+1),d,n-1,n-m,(-1)**(D-d))
        c = (m-d+1)/d * (n-1)/(n-m) * ((-1)**d + c)
#        print(c)
        d -= 1
        n -= 1
        
    return (c + 1) * binomial(n-d-1,m-1)

# factorials probably simplify though

# (n-d-1)!/(n-d-m)*(
# (-1)**d     * m!/(0!m!) +
# (-1)**(d-1) * m!/(1!(m-1)!) * (n-d)/(n-d-m+1) +
# (-1)**(d-2) * m!/(2!(m-2)!) * (n-d)(n-d+1)/((n-d-m+1)((n-d-m+2)) +
# 
    
# We'll calculate the first factorial "by hand"
#
# 
n = 10000000000000
m = 1000000000000
d = 10000

n = 100
m = 10
d = 4

i = n-m-d+1
j = i+1
j_max = n-d

while j < j_max:
    i *= j
    j += 1

k = 0
c = 1/(m-k)*(n-d-m+1)/(n-d+1)

while k < d:
#        print((m-d+1),d,n-1,n-m,(-1)**(D-d))
    c += (-1)**k * (k+1)/(m-k)*(n-d-m+k+1)/(n-d+k+1) * c
    print(c)
    k += 1
