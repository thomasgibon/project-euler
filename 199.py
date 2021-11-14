# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 23:30:42 2021

@author: Gibon
"""

from sympy import *
from itertools import combinations

a,b,c,r,r1,r2,r3,R,A,B,C,D,cos=symbols('a b c r r1 r2 r3 R A B C D cos')

# a=sqrt((r2*r3)/(r**2+r*(r2+r3)))
# b=sqrt((r1*r3)/(r**2+r*(r1+r3)))
# c=sqrt((r1*r2)/(r**2+r*(r1+r2)))

# t=(a+b+c-a*b*c)/(1-a*b-b*c-a*c)

# sols=solve(t,r)

# # sols[3] seems to be the non-trivial positive

# A=sqrt((r2*r3)/(R**2-R*(r2+r3)))
# D=sqrt((r2*r3)/(r**2+r*(r2+r3)))
# B=sqrt((r*R)/(r3*(R-r)-r3**2))
# C=sqrt((r*R)/(r2*(R-r)-r2**2))

# T=(A+B+C+D-A*B*C-A*C*D-A*B*D-B*C*D)/(1-A*B-B*C-C*D-A*C-B*D-A*D+A*B*C*D)

# SOLS=solve(T,r)

def r_inner(r1,r2,r3):
    
    k,k1,k2,k3,r=symbols('k k1 k2 k3 r')
    
    k1=(1/r).subs({r:r1})
    k2=(1/r).subs({r:r2})
    k3=(1/r).subs({r:r3})
    
    k = k1 + k2 + k3 + 2*sqrt(k1*k2+k2*k3+k3*k1)
    
    return simplify(1/k)

def r_outer(r1,r2,r3):
    
    k,k1,k2,k3,r=symbols('k k1 k2 k3 r')
    
    k1=(1/r).subs({r:r1})
    k2=(1/r).subs({r:r2})
    k3=(1/r).subs({r:r3})
    
    k = k1 + k2 + k3 - 2*sqrt(k1*k2+k2*k3+k3*k1)
    
    return simplify(1/k)


def radii(n):
    
    if n==0:
        return [-1,-3 + 2*sqrt(3),-3 + 2*sqrt(3),-3 + 2*sqrt(3)]

r_list0 = [-1,-3 + 2*sqrt(3),-3 + 2*sqrt(3)]
r_list = r_list0

global area_sum

def area_calc(n, r_list, area_sum=0):
    
    r=r_inner(*r_list)
    
    if n==0:
        return area_sum
    
    if n>0:
        print(n,area_sum)
        area_sum += N(pi*r*r)
        for r_subset in combinations(r_list,2):
            area_calc(n-1, [r]+list(r_subset), area_sum)