# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:48:55 2015

@author: gibon
"""

def fib(k):
    if k in {1,2}:
        return 1
    F = [1,1]
    for i in range(k-2):
        F.append(sum(F))
        F.pop(0)
    return F[-1]

phi = (1+5**.5)/2

k = 10000
F = fib(k)
f = [fib(k-1), fib(k)]

while set(str(int(F))[:9]) != s or set(str(f[-1])[-9:]) != s:
    k += 1
    F = int(str(int(F))[:20]) * phi
    f.append(sum(f)%10**12)
    f.pop(0)

print('Answer is {}'.format(k))

#import numpy as np
#from decimal import *
#
#F, F_first, F_last = [[1,1]]*3
#k = 2
#s = set([str(d) for d in range(1,10)])
#
#lastpan  = []
#firstpan = []
#

#while set(str(F[-1]).zfill(10)[-9:]) != s:# or set(str(F[-1]).zfill(10)[:9]) != s:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#    k += 1
#    if k%1000 == 0:
#        print(k)
#    F.append(sum(F))
#    F.pop(0)
#
#print('Found F_{} = {}'.format(k,F[-1]))
#
#k = 2
#F, F_first, F_last = [[1,1]]*3
#
#while set(str(F[-1]).zfill(10)[:9]) != s:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#    k += 1
#    if k%1000 == 0:
#        print(k)
#    F.append(sum(F))
#    F.pop(0)
#    
#print('Found F_{} = {}'.format(k,F[-1]))
##
#F, F_first, F_last = [[1,1]]*3
#
#for k in range(2,10**6):
#    if set(str(F_last[-1]).zfill(9)[-9:]) == s:
#        lastpan.append(k)
#        print(k,F_last[-1])
#    F_last.append(sum(F_last)%10**9)
#    F_last.pop(0)
##
#F, F_first, F_last = [[1,1]]*3
#
#for k in range(2,10**6):
#    if set(str(F_first[-1])) == s:
#        firstpan.append(k)
#        print(k,F_first[-1])
#    F_next = sum(F_first)
#    F_first.append(sum(F_first)//10**len())
#    F_first.pop(0)
##
##F_first = [[1,0]]*2
#
#k = 2
#F, F_first, F_last = [[1,1]]*3
#
#while set(str(F_last[-1]).zfill(10)[-9:]) != s or set(str(F_first[-1]).zfill(10)[:9]) != s:
#    k += 1
#    if k%1000 == 0:
#        print(k)
#    F_last.append(sum(F_last)%10**12)
#    F_first.append(float(format(sum(F_first),".20e")))
#    F_last.pop(0)
#    F_first.pop(0)
#    
#print('Found F_{} = {}'.format(k,F[-1]))

#def sum_log(a,b):
#    if a[1] > b[1]:
#        N, n = a, b
#    if a[1] < b[1]:
#        N, n = b, a
#    if a[1] == b[1]:
#        if a[0] > b[0]:
#            N, n = a, b
#        if a[0] < b[0]:
#            N, n = b, a
#    s = n[0]+N[0]*10**(N[1]-n[1])
#    p = int(np.log10(s) + N[1])
#    return [s*10**-(p-N[1]),p]
