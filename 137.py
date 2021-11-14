# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:36:48 2015

@author: gibon
"""

from numpy import pi, cos

def F(n):
    if n in {0,1,2}:
        return 1
    F_list = [1,2]
    for k in range(n - 3):
        f = F_list[1]
        F_list[1] = sum(F_list)
        F_list[0] = f
    return F_list[1]
    
def A_F(x):
    i_max = 1000
    F_list = [1,1]
    x_sum = x + x**2
    for i in range(1,i_max):
        f = F_list[i] + F_list[i-1]
        x_sum += x**(i+2)*f
        F_list.append(f)
    return x_sum

def F_real(x):
    """
    Fibonacci for real numbers
    """
    return 5**-.5*(((1+5**.5)/2)**x-(2/(1+5**.5))**x*cos(pi*x))

def A_F_recip(a):
    """
    A_F's reciprocal
    """
    return (-(1+1/a)+((1+1/a)*(1+1/a)+4)**.5)/2

"""
A_F_recip is rational for sqrt((1+1/a)**2+4) rational

i.e. for 5*a**2 + 2*a + 1 square

http://math.stackexchange.com/questions/68944/determine-if-equation-will-generate-perfect-squares
"""

def fib_nugget(n):
    return F(2*n)*F(2*n+1)
    
n = fib_nugget(15)

print('Solution to problem 137 is %i.'%n)