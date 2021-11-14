# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:50:15 2015

@author: gibon
"""

import networkx as nx

def P(s,n):
    return int((s - 2) * n * (n - 1) / 2 + n)

def is_P(p):
    n_list = []
    for s in range(3,9):
        n = ((8*p*s-16*p+s**2-8*s+16)**.5+s-4)/(2*(s-2))
        if int(n) == n:
            n_list.append((s,int(n)))
    return n_list

# Determine boundaries
p_min = 1000
p_max = 9999
n_min = []
n_max = []

for s in range(3,9):
    n_min.append(int(((8*p_min*s-16*p_min+s**2-8*s+16)**.5+s-4)/(2*(s-2))) + 1)
    n_max.append(int(((8*p_max*s-16*p_max+s**2-8*s+16)**.5+s-4)/(2*(s-2))))

options = []

for i in range(len(n_min)):
    options.append([P(i+3,n) for n in range(n_min[i],n_max[i] + 1)])

chains = {}

G = nx.DiGraph()

for k in range(5,-2,-1):
    for i in options[k]:
        for j in options[k-1]:
            if str(i)[2:] == str(j)[:2]:
                G.add_edge(i,j)
    
halves = []

for option in options:
    first_half  = set([str(p)[:2] for p in option])
    second_half = set([str(p)[2:] for p in option])
    halves.append((first_half,second_half))

ind = set(range(6))

