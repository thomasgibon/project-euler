# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:44:15 2015

@author: gibon
"""

import urllib

file_url = 'https://projecteuler.net/project/resources/p081_matrix.txt'
matrix   = [[int(n) for n in row.split(',')] for row in 
urllib.request.urlopen(file_url).read().decode('utf-8').split()]

l = len(matrix)

tri1 = []
tri2 = []

for diag in range(l):
    row1 = []
    row2 = []
    for i in range(diag + 1):
        row1.append(matrix[i][diag-i])
        row2.append(matrix[l-i-1][l-(diag-i+1)])
    tri1.append(row1)
    tri2.append(row2)

tri2.reverse()

s = 0
m_list = []

tri = tri2

for row in tri:
    while len(tri) > 2:
        t0 = tri.pop()
        t1 = tri.pop()
        m  = [min(t0[i],t1[i+1]) + t for i,t in enumerate(t1)]
        tri.append(m)
        m_list.append(m)
    s += tri[0][0]

tri1[-1] = [tri2[1][0] + t for t in tri2[0]]

tri = tri1

for row in tri:
    while len(tri) > 1:
        t0 = tri.pop()
        t1 = tri.pop()
        m  = [min(t0[i],t0[i+1]) + t for i,t in enumerate(t1)]
        tri.append(m)
        m_list.append(m)
    s += tri[0][0]