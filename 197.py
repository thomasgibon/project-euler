# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 21:00:07 2021

@author: Gibon
"""

def f(x):
    
    return int(2**(30.403243784-x*x))*1e-9

def u(n):
    
    if n==0:
        return -1
    while n>0:
        return f(u(n-1))

u=-1
u_next=f(u)
s=u_next+u
s_next=f(u_next)+u_next
epsilon = 1e-9
count=0

while abs(s_next-s)>epsilon:
    count+=1
    s=s_next
    u=u_next
    u_next=f(u)
    s_next=f(u_next)+u_next
    print(s,s_next)
    
print(count,s_next)