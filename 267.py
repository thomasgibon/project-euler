# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 18:32:42 2021

@author: Gibon
"""

import math
import numpy as np
import pandas as pd

def C(n,f):
    # capital after n throws for factor f in [0,1]

    if n==0:
        return 1
    else:
        return 1/2*C(n-1,f)*(2+f)

def combs(k,n):
    return int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))

f=1/4
n=1000
res=[(combs(k,n),
      (1+2*f)**k*(1-f)**(n-k)) for k in range(n+1)]

res= [(f,sum(combs(k,n) for k in range(n+1) \
             if (1+2*f)**k*(1-f)**(n-k)>1e9)/2**1000)\
                  for f in np.linspace(0,.9,11)]


def beta(n=1000, span=(0,1), n_points=11):

    count_list = []

    for f in np.linspace(span[0],span[1],n_points):
        count=0

        for k in range(n+1):
            if (1+2*f)**k*(1-f)**(n-k) >= 1e9:
                count += combs(k,n)

        count_list.append((f,count/2**1000))

    return count_list

f_list = beta(n_points=101, span=(0.1,0.2))

sol=max(s[1] for s in f_list)