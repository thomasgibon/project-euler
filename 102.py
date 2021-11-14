# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:45:56 2015

@author: gibon
"""

import urllib

file_url = 'https://projecteuler.net/project/resources/p102_triangles.txt'

triangles = [list(map(int,row.split(','))) for row in 
urllib.request.urlopen(file_url).read().decode('utf-8').split()]

def is_point_in_triangle(p,ABC):
    x,y = p
    xa,ya,xb,yb,xc,yc = ABC
    
    x0,y0 = (xa,ya)    
    x1,y1 = (xb-xa,yb-ya)
    x2,y2 = (xc-xa,yc-ya)
    
    a = ((x * y2 - x2 * y) - (x0 * y2 - x2 * y0))/\
        (x1 * y2 - y1 * x2)
    b = - ((x * y1 - x1 * y) - (x0 * y1 - x1 * y0))/\
          (x1 * y2 - y1 * x2)
    if a > 0 and b > 0 and a + b < 1:
        return True
    return False

p = (0,0)

n = sum([is_point_in_triangle(p,ABC) for ABC in triangles])

print('Solution to problem 102 is %i.'%n)