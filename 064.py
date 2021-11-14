# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 23:08:36 2015

@author: gibon
"""

import time

def sqrt_cycle_length(k):
    
    if not isinstance(k, int) or k <= 0:
        raise ValueError("cycle_length(d): d must be a positive integer")
    
    alist     = [] # list of remainder
    l = 0
    m = 0
    d = 1
    a = int(k**.5)
    
    a0 = a
    if a0**2 == k:
        return 0, a0, 0
    
    if a0**2 == k - 1:
        return 1, a0, 2*a0
        
    while a:
        m = d * a - m
        d = (k - m**2)/d
        a = int((a0 + m)/d)
        alist.append(a)
        l += 1
        if a == 2 * a0:
            return l, a0, alist
#        if l%2 == 0:
#            p = int(l/2)
#            if alist[:p] == alist[p:] and a > 1:
#                return p, a0, alist[:p]
    return 0

start_time = time.time()

if __name__ == '__main__':
    ub = 10000
    i = 0
    for d in range(1,ub + 1): #d = raw_input('d: ')
        try:
            c = sqrt_cycle_length(int(d))
#            print('root of %i has period' % (d), c)
            if c[0] % 2 == 1:
                i += 1
        except ValueError:
            print('invalid input')

print(i, 'in', time.time()-start_time, 'secs')