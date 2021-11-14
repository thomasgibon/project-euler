# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:02:51 2020

@author: Gibon
"""

from itertools import permutations, product
import pandas as pd
import tqdm
from sympy import *

Sigma = {'a','b','c'}

def words(Sigma,k):
    return [(''.join(s),set(s) == Sigma) for s in  product(Sigma,repeat=k)]

#completeness_dict = {0:{'complete':0,'incomplete':1}}
#
#for k in tqdm.trange(10):
#    completeness_dict.update({k:{'complete':sum(w[1]==1 for w in words(Sigma,k)),
#                                 'incomplete':sum(w[1]==0 for w in words(Sigma,k))}})
#    
#completeness_df = pd.DataFrame.from_dict(completeness_dict, orient='index')
#completeness_df.index.name = 'word_length'
#completeness_df['n_words'] = completeness_df.sum(1)

#completeness_df.divide(completeness_df.sum(1),axis=0).plot()

def I_rec(alpha, n):
    
    m = 0
    I = 0
    
    while m <= n:
        
        k = 0
        
        while k < alpha:
            i = binomial(alpha,k) * (-1)**(alpha-k+1) * (k)**m
            print(m,k,i)
            I += i
            k += 1
            
        m += 1
        
    return I

def i_list(alpha,n):
    
    if alpha + n == 0:
        return [0]
    if alpha == 1 and n>0:
        return [0]
    return [1,
            (-1)**alpha * alpha * n] + \
            [binomial(alpha,k) * (-1)**(alpha-k+1) * (k**(n+1)-k)/(k-1) for k in range(2,alpha)]

def sum_alt_integers(fro=2,to=10):
    
    return to*((to-fro+1)%2) - (to-fro+1)//2

def S(k,n):
#    mod = 10000000000
    S = n # % mod
#    
    
    a = 1
    
    while a <= k:
        
        S += ((-1)**a * a * n + 1) # % mod
        p = 2
        
        while p < a:
            i = binomial(a,p) * (-1)**(a-p+1) * (p**(n+1) - p)/(p - 1)
            S += i # % mod
    #        print(a,p,S,i)
            p += 1
        a += 1

    return S

mod = 1000000007
#print(S)
    
# Check for S(10,100)
print(sum([sum(i_list(a,100)) for a in range(0,10+1)]) % 1000000007 == 983602076)

print(S(4,4) == 406,
      S(8,8) == 27902680,
      S(10,100)%mod == 983602076)

#S(1000,1000)
