# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:40:03 2015

@author: gibon
"""

from sympy import factorint, divisor_count
import numpy as np
from collections import Counter
import itertools

def partitions(set_): # From http://stackoverflow.com/questions/2037327/translating-function-for-finding-all-partitions-of-a-set-from-python-to-ruby
    if not set_:
        yield []
        return
    for i in range(int(2**len(set_)/2)):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def algorithm_u(ns, m): # From http://codereview.stackexchange.com/questions/1526/finding-all-k-subset-partitions
    def visit(n, a):
        ps = [[] for i in range(m)]
        for j in range(n):
            ps[a[j + 1]].append(ns[j])
        return ps

    def f(mu, nu, sigma, n, a):
        if mu == 2:
            yield visit(n, a)
        else:
            for v in f(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v
        if nu == mu + 1:
            a[mu] = mu - 1
            yield visit(n, a)
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                yield visit(n, a)
        elif nu > mu + 1:
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = mu - 1
            else:
                a[mu] = mu - 1
            if (a[nu] + sigma) % 2 == 1:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v

    def b(mu, nu, sigma, n, a):
        if nu == mu + 1:
            while a[nu] < mu - 1:
                yield visit(n, a)
                a[nu] = a[nu] + 1
            yield visit(n, a)
            a[mu] = 0
        elif nu > mu + 1:
            if (a[nu] + sigma) % 2 == 1:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] < mu - 1:
                a[nu] = a[nu] + 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = 0
            else:
                a[mu] = 0
        if mu == 2:
            yield visit(n, a)
        else:
            for v in b(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v
                
    n = len(ns)
    a = [0] * (n + 1)
    for j in range(1, m + 1):
        a[n - m + j] = j - 1
    return f(m, n, 0, n, a)

def dioph_reciprocals(N):
    facts = factorint(N)
    facts.update({1:2})
    
    all_facts = []
    for k,v in facts.items():
        all_facts.extend([k]*v)
    
    kmns = tuple(set(tuple(np.prod(i) for i in j) for j in algorithm_u(all_facts,3)))
    
    sols = []
    
    for triplet in kmns:
        for k,m,n in itertools.permutations(triplet):
            d = k*(m + n)
            sols.append(tuple(sorted((m*d,n*d))))
    
    sols.append((2*N,2*N))
    return set(sols)

def dioph_reciprocals_count(N):
    return int((np.prod([(2*k+1)**v for k,v in Counter(factorint(N).values()).items()])+1)/2)

if __name__ == "__main__":

    # le nombre de solutions d'un réciproque diophantin est
    # (produit((2*k_i + 1)**(nombres de puissance k_i)) + 1)/2
    # 
    
    ub = 1000 
    count = 0
    k = 1
    
    while count < ub:
        k += 1
        count = dioph_reciprocals_count(k)
    
    n = k
    
print('Solution to problem 108 is %i.'%n)
    