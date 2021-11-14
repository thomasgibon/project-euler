# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:57:50 2020

@author: Gibon



Given the positive integers, x, y, and z, are consecutive terms of an
arithmetic progression, the least value of the positive integer, n, for which
the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?

--- simplifying the problem

x, y, and z and in arithmetic progression, and x > y (for n > 0) so

for any integer x, y = x - r and z = x - 2r

rewrite:
    x2 − y2 − z2 = n
    6rx - 5r2 - x2 = n
    x2 - 6rx + 5r2 + n = 0
    (x - 3r)2 - (4r2 - n) = 0
    (x - 3r - sqrt(4r2 - n)) * (x - 3r + sqrt(4r2 - n)) = 0
    
which is true iff:
    x - 3r = +- sqrt(4r2 - n)

iff:
    4r2 - n is a perfect square

so:
    4r2 - n = k2
    n = 4r2 - k2 = (2r - k)(2r + k)
    
if n can be written as the product of two integers with a difference of 2k and
average of 2r, then there is a solution.

E.g. n = 27 can be written as a product of 3 and 9, averaging 6 => r = 3
                                        of 1 and 27, averaging 14 => r = 7

Then x = sqrt(4r2 - n) + 3r

"""

def first_divisors(n):
    divs = []
    for i in range(1,int(n**.5)+1):
        if n%i == 0:
            divs.append(i)
    return divs

def potential_rs(n):
    r_list = []
    for i in range(1,int(n**.5)+1):
        if n%i == 0:
            rr = (i + n//i) # twice (2*) the average, which needs to be even (2*)
            if rr%4 == 0:   # so we test division by 4
                r_list.append(rr//4)
    return r_list

def all_solutions(n):
    rx_list = []
    for i in range(1,int(n**.5)+1):
        if n%i == 0:
            rr = (i + n//i) # twice (2*) the average, which needs to be even (2*)
            if rr%4 == 0:   # so we test division by 4
                r = rr//4
                d = int((4*r*r-n)**.5)
                x = 3*r + d
                rx_list.append([r,x])
                if n > 3*r*r and n != 4*r*r:
                    rx_list.append([r,x-2*d])
    return rx_list
                    
def count_solutions(n, check=None):
    
    if n%4 in (1,2): # if n = 4k+{1,2} then it has divisors 4k+1, 1
        if check:
            return check==0
        else:
            return 0
    
    c = 0

    for i in range(1,int(n**.5)+1):
        if n%i == 0:
            rr = (i + n//i)
            if rr%4 == 0:
                c += 1
                r = rr//4
                if n > 3*r*r and n != 4*r*r:
                    c += 1
    if check:
        return c==check
    else:
        return c

# Faster
n_max = 1000000
n_to_test = sorted(list(range(0,n_max,4)) + list(range(3,n_max,4)))

c = 0
for n in n_to_test:
    if n%10000 == 0:
        print(n,c)
    c += count_solutions(n,10)