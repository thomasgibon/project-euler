# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:04:18 2016

@author: gibon
"""

import sympy

def digitalroot(k):
    k_list = [k]
    while len(str(k_list[-1])) > 1:
        k_list.append(sum(int(d) for d in str(k_list[-1])))
    return k_list

'''
  1
2   3
  4
5   6
  7
'''

segments = \
{'1':{3,6},
 '2':{1,3,4,5,7},
 '3':{1,3,4,6,7},
 '4':{2,3,4,6},
 '5':{1,2,4,6,7},
 '6':{1,2,4,5,6,7},
 '7':{1,2,3,6},
 '8':{1,2,3,4,5,6,7},
 '9':{1,2,3,4,6,7},
 '0':{1,2,3,5,6,7},
 'E':set()}

## On Max's clock
#on  = segments[3]
#off = segments[1] & segments[3]
#on  = segments[1] - segments[3]

def Sam(k):
    dr = digitalroot(k)
    c = 0
    for r in dr:
        on_off = 2 * sum(len(segments[digit]) for digit in str(r))
        c += on_off
    return c

def Max(k):
    # initialization
    on = sum(len(segments[digit]) for digit in str(k))
    c = on
#    print(on)
    dr = digitalroot(k)
    
    l = len(str(k)) # number of digits in the clock
    
    for i,_ in enumerate(dr[:-1]):
        off = [len(segments[digit_off] - segments[digit_on]) for digit_off, digit_on in zip(str(dr[i]).rjust(l,'E'), str(dr[i + 1]).rjust(l,'E'))]
        on  = [len(segments[digit_on] - segments[digit_off]) for digit_off, digit_on in zip(str(dr[i]).rjust(l,'E'), str(dr[i + 1]).rjust(l,'E'))]
#        print(sum(off), sum(on))
        c += sum(off) + sum(on)
    
    off = len(segments[str(dr[-1])])
    c += off
#    print(off)
    
    return c

if __name__ == '__main__':
    
    N = 0
    A = 1e7
    B = 2e7
    
    for i, p in enumerate(sympy.ntheory.primerange(A,B)):
        if i%1000 == 0:
            print(i,p)
            
        N += Sam(p) - Max(p)