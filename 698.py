# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:08:58 2020

@author: Gibon

 We define 123-numbers as follows:

    1 is the smallest 123-number.
    When written in base 10 the only digits that can be present are "1", "2" and "3" and if present the number of times they each occur is also a 123-number.

So 2 is a 123-number, since it consists of one digit "2" and 1 is a 123-number. Therefore, 33 is a 123-number as well since it consists of two digits "3" and 2 is a 123-number.
On the other hand, 1111 is not a 123-number, since it contains 4 digits "1" and 4 is not a 123-number.

In ascending order, the first 123-numbers are:
1,2,3,11,12,13,21,22,23,31,32,33,111,112,113,121,122,123,131,…

Let F(n)
be the n-th 123-number. For example F(4)=11, F(10)=31, F(40)=1112, F(1000)=1223321 and F(6000)=2333333333323

.

Find F(111111111111222333)
. Give your answer modulo 123123123. 
"""

import pandas as pd
from collections import Counter
from itertools import permutations, product
from math import factorial as fact

import matplotlib.pyplot as plt


def check123(n, verbose=False):
    
    if n == 1:
        return True
    
    count = Counter(str(n))
    
    if verbose:
        print('{} contains '.format(n) + ', '.join('{} "{}"'.format(v,k) for k,v in count.items()))
    
    non123 = set(count.keys()) - {'1','2','3'}
    
    if non123 != set():
        if verbose:
            print('{} is not an 123-number!'.format(n))
        return False
    
    return all(check123(v) for v in count.values())

test_list = [''.join(p) for r in (1,2,3,4,5,6,7,8,9,10,12,13,14) for p in product(['1','2','3'],repeat=r)]
count123  = [(n,c+1) for c,n in enumerate(int(t) for t in test_list if check123(t))]

count123_df = pd.DataFrame(count123, columns=['123-number','F']).set_index(['123-number'])
#count123_df.plot(logx=True, logy=True)

# count123_df.loc[2333333333323]
# Out[493]: 
# F    6000
# Name: 2333333333323, dtype: int64


def generate123():
    
    list123 = [1,2,3]
    
    count = 3
    
    while len(list123) < 10:
        for r in list123:
            for prod in product([1,2,3],repeat=r):
                count += 1
                if count%1e5==0:
                    print(count)
                list123.append(int(''.join([str(p) for p in prod])))
                
#        new123 = [int(''.join([str(p) for p in prod])) for r in list123 for prod in product(list123,repeat=r)]
#        list123.extend(new123)
        
# This seems to be relevant https://math.stackexchange.com/questions/975503/how-many-ways-to-place-n-distingusishable-balls-into-m-distinguishable-bins-of-s
        
def partitionfunc(n,k,mi=1):
    '''
    n is the integer to partition,
    k is the length of partitions,
    mi is the min partition element size
    '''
    
    if k < 1:
        return
    if k == 1:
        if mi <= n:
            yield (n,)
        return
    for i in range(mi,n+1):
        for result in partitionfunc(n-i,k-1,i):
            yield (i,)+result
            
def count123digits(k):
    
    valid123 = {1,2,3,11,12,13,21,22,23,31,32,33}
    count_list = []
    
    for r in range(k):
        
        partitions = {1:[],2:[],3:[]}
        partitions.update({le:[p for p in partitionfunc(r,le) if set(p).issubset(valid123)] for le in range(1,4)})
        
        count = 3*len(partitions[1])
        
        for p in partitions[2]:
            count += 3*fact(r)/(fact(p[0])*fact(p[1]))*len(set(p))
        
        for p in partitions[3]:
            l = len(set(p))
            count += fact(r)/(fact(p[0])*fact(p[1])*fact(p[2]))*l*(l+1)/2
    
        count_list.append((r,int(count)))
        
    return pd.DataFrame([(10**r,r,c) for r,c in count_list]).set_index(0)

t = 111111111111222333

c = count123digits(50)
c['cumul'] = c[2].cumsum()

print(c.iloc[37:39,:]['cumul'] - t)
# the answer has 38 digits

#
#new_index = sorted(c.index.tolist() + count123_df.index.tolist())
#
#pd.concat([c.reindex(new_index), count123_df.reindex(new_index)]).plot(logx = True)

c = count123digits(100)
c['cumul'] = c[2].cumsum()
plt.plot(c['cumul'])
plt.plot(count123_df)
plt.plot((1,1e39),(t,t))
plt.loglog()
plt.text(x=1,y=2*t,s=str(t))
