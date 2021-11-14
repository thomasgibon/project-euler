# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:04:48 2015

@author: gibon
"""

f = open('p067_triangle.txt', 'r')
data = [line for line in f.readlines()]

tri = [[int(num) for num in line.split()] for line in data]
ml  = []
path = []

while len(tri) > 1:
    t0 = tri.pop()
    t1 = tri.pop()
    m  = [max(t0[i],t0[i+1]) + t for i,t in enumerate(t1)]
    tri.append(m)
    ml.append(m)
    
for k in range(len(ml)-1,-1,-1):
    path.append([(i,m) for i,m in enumerate(ml[k]) if m == max(ml[k])])

n = tri[0][0]

print('Solution to problem 67 is %i.'%n)