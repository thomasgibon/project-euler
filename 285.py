# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:03:13 2020

@author: Gibon
"""

from  sympy import *

# The equation is

# (k-.5)^2 < (ka+1)^2 + (kb+1)^2 < (k+.5)^2

# see https://www.desmos.com/calculator/8d5wek6qed
# https://www.desmos.com/calculator/l0ywuvb5kv
# https://www.desmos.com/calculator/mjspb4oxxn

x,y,k = symbols('x y k')

alpha_l = asin(1/(k-1/2))
alpha_u = asin(1/(k+1/2))

m_l = ((1-1/(2*k))**2 - (1/k)**2)**(1/2)
m_u = ((1+1/(2*k))**2 - (1/k)**2)**(1/2)

A_l = m_l/(2*k) + 1/2 * alpha_l * (1-1/(2*k))**2
A_u = m_u/(2*k) + 1/2 * alpha_u * (1+1/(2*k))**2

A_lq = Piecewise((0, Eq(k, 1)), (pi/4*(1-1/(2*k))**2 - 2*A_l + 1/k**2, True))
A_uq = pi/4*(1+1/(2*k))**2 - 2*A_u + 1/k**2

A = A_uq - A_lq

s = 0

for m in range(1,100001):
    s += m * N(A.subs(k,m))

print(s)