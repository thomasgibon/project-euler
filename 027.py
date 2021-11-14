# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:42:27 2015

@author: gibon
"""

import numpy as np

def isprime(k):
    if k <= 0:
        return False
    elif k == 2:
        return True
    else:
        i = 2
        while i <= int(k**0.5):
            if k % i == 0:
                return False
            i += 1
        return True
        
if __name__ == '__main__':
    lb = -1000
    ub = 1000
    test_range = range(lb,ub)
    
    # limit the range for b to primes
    primes = [p for p in test_range if p > 0 and isprime(p)]
    
    x_max = 0
    
    for a in test_range:
        for b in primes:
            x = 0
            c = (1,a,b)

            while isprime(np.polyval(c,x)):
                x += 1
            if x > x_max:
                a_max, b_max, x_max = a,b,x
            
    n = a_max * b_max
    
    print('Solution to problem 27 is %i (n^2 + %i n + %i gives %i primes).'%(n, a_max, b_max, x_max))