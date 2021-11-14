# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:40:03 2015

@author: gibon
"""

from sympy import factorint, sieve

# Voir 108
# La question revient à trouver les plus petits k_i pour produit((2*k_i+1)**v_i) > 2*4000000 - 1
# Évidemment on peut remonter les produits de premiers...

ub = 2*4*10**6-1

minimum = 5

for i in range(ub,ub+100000,2):
    k = max(list(factorint(i).keys()))
    if k < minimum:
        minimum = k
        n = i

blocks = sorted([[int((k-1)/2)] * v for k,v in factorint(n).items()], reverse = True)
blocks = [item for sublist in blocks for item in sublist]

m = 1

for prime, p in zip(list(sieve._list[:len(blocks)]),blocks):
    print(prime**p)
    m *= prime**p

n = m

print('Solution to problem 110 is %i.'%n)