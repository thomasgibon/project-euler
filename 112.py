# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:40:55 2015

@author: gibon
"""

def bouncy(k):
    """Counts bouncy numbers under k"""
    inc = 0
    dec = 0
    for i in range(1,k+1):
        s = str(i)
        ci = sum([int(s[j + 1]) >= int(s[j]) for j in range(len(s) - 1)])
        cd = sum([int(s[j + 1]) <= int(s[j]) for j in range(len(s) - 1)])
        if ci == len(s) - 1:
            inc += 1
        elif cd == len(s) - 1:
            dec += 1
    bouncy = k - dec - inc
    return bouncy/k

def isbouncy(k):
    s = str(k)
    ci = sum([int(s[j + 1]) >= int(s[j]) for j in range(len(s) - 1)])
    cd = sum([int(s[j + 1]) <= int(s[j]) for j in range(len(s) - 1)])
    if not (ci == len(s) - 1 or cd == len(s) - 1):
        return True
    else:
        return False

i = 0
rate = 0
b = 0

while rate < .99:
    i += 1
    b += isbouncy(i)
    rate = b/i

n = i

print('Solution to problem 112 is %i.'%n)