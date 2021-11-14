# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:05:46 2016

@author: Thomas
"""

def sqchain(n):
    k = sum(int(d)*int(d) for d in str(n))
    if k == 1 or k == 89 or n == 89:
        return [n,1]
    chain = [n]
    while k not in {1, 89}:
        k = sum(int(d)*int(d) for d in str(k))
        chain.append(k)
    return chain

def calcsink(k):
    return sqchain(k)[-1]
    
if __name__ == '__main__':
    
    NMAX = 10000000
    sink = {1:1, 89:89}
    
    for n in range(NMAX, 0, -1):
        chain = [n]
        k = sum(int(d)*int(d) for d in str(n))
        while k not in sink.keys():
            k = sum(int(d)*int(d) for d in str(k))
            chain.append(k)
        sink.update(dict.fromkeys(chain, sink[k]))
        if n%100000 == 0:
            print((n,len(sink)))

    print('The solution is {}.'.format(sum(x == 89 for x in sink.values())))