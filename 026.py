# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:52:56 2015

@author: gibon

from http://codereview.stackexchange.com/questions/39642/helper-function-to-solve-project-euler-question-26
"""

def cycle_length(d):
    
    if not isinstance(d, int) or d <= 0:
        raise ValueError("cycle_length(d): d must be a positive integer")
        
    rlist     = [] # list of remainder
    qlist_len = 0
    remainder = 1
    
    while remainder:
        remainder = remainder % d
        if remainder in rlist:
            return qlist_len - rlist.index(remainder)
        rlist.append(remainder)
        remainder *= 10
        qlist_len += 1
        
    return 0

c_max = [0,0]

if __name__ == '__main__':
    for d in range(1,1000): #d = raw_input('d: ')
        try:
            c = cycle_length(int(d))
            print('1/%s =' % (d), c)
            if c > c_max[1]:
                c_max[1] = c
                c_max[0] = int(d)
        except ValueError:
            print('invalid input')
    
    print('Solution to problem 26 is %i (cycle %i).'%(tuple(c_max)))