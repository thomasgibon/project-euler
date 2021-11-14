# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:43:23 2015

@author: gibon
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

precision = 30

def line(xy0,xy1):
    """gives a, b and c for a * x + b * y + c = 0 equation
    of the line joining 0 and 1"""
    a = xy1[1] - xy0[1]
    b = xy0[0] - xy1[0]
    c = - a * xy1[0] - b * xy1[1]
    return (a,b,c)

def intersect(abc,ABC):
    """intersection(s) of line ax + by + c = 0
    and ellipse Ax^2 + By^2 + C = 0 if they exist"""
    (a,b,c) = abc
    (A,B,C) = ABC
    
#    Dx = a**2 * B**2 * c**2 - \
#        (A * b**2 + a**2 * B) * (B * c**2 + b**2 * C)
    
    Dx = - b**2 * (a**2 * B * C + A * b**2 * C + A * B * c**2)
    
    x1 = (- a * B * c - Dx**.5) / (A * b**2 + a**2 * B)
    x2 = (- a * B * c + Dx**.5) / (A * b**2 + a**2 * B)
    
#    Dy = A**2 * b**2 * c**2 - \
#        (A * b**2 + a**2 * B) * (A * c**2 + a**2 * C)
    
    Dy = - a**2 * (a**2 * B * C + A * b**2 * C + A * B * c**2)    
    
#    y1 = (- A * b * c + Dy**.5) / (A * b**2 + a**2 * B)
#    y2 = (- A * b * c - Dy**.5) / (A * b**2 + a**2 * B)
    
    y1 = (- c - a * x1)/b
    y2 = (- c - a * x2)/b
    
    if Dx >= 0 and Dy >= 0:
        return ((x1,y1),(x2,y2))
    else:
        return False

def bounce(v1,v2):
    """incident line with vector v1 bounces on line with vector v2
    returns the reflective vector v3
    (with same norm as incident v1)"""
    
    (x1,y1) = v1
    v2_norm = sum((i**2 for i in v2))**.5
    (x2,y2) = (i/v2_norm for i in v2)
    
    x3 = (x2**2 - y2**2) * x1 + 2 * x2 * y2 * y1
    y3 = (y2**2 - x2**2) * y1 + 2 * x2 * y2 * x1
    
    v3 = (x3,y3)
    return v3

def plotellipse(ABC):
    """plots and ellipse with coefficients ABC
    y = ± (C - Ax)**.5/B"""
    A,B,C = ABC
    fig = plt.figure()  
    ax = fig.add_subplot(111, aspect = 'equal')
    x_half = (-C/A)**.5
    y_half = (-C/B)**.5
    ax.add_artist(mpl.patches.Ellipse(xy=(0,0), width=2*x_half, height=2*y_half, alpha = 0.1))
    padding = min([x_half,y_half])/2
    ax.set_xlim(- x_half - padding, x_half + padding)
    ax.set_ylim(- y_half - padding, y_half + padding)
    return ax

# The tangent line has vector (-4 * x, y)

opening = (-.01,.01)

(x0,y0) = (0.0,10.1)
(x1,y1) = (1.4,-9.6)

(A,B,C) = (4,1,-100)

ax         = plotellipse((A,B,C))
xmin, xmax = ax.get_xlim()

i = 0

while not (opening[0] <= x1 <= opening[1] and y1 > 0):

    i += 1
    
    xy0 = (x0,y0)
    xy1 = (x1,y1)
    
#    print("---")
#    print(xy0)
#    print(xy1)
#    print("---")    
    
    (a,b,c) = line(xy0,xy1)
    v1 = (- b, a)           # incident ray
    v2 = (- B * y1, A * x1) # reflection surface
    v3 = bounce(v1,v2)      # reflected ray
    
    d = v3[1]
    e = - v3[0]
    f = - d * x1 - e * y1
    
    p = v2[1]
    q = - v2[0]
    r = - p * x1 - q * y1
    
    l = mpl.lines.Line2D([x0,x1],[y0,y1],color = 'red')   
    m = mpl.lines.Line2D([xmin,xmax],[(- p * xmin - r)/q,(- p * xmax - r)/q])
    ax.add_line(l)
    ax.add_line(m)
    
    (x0,y0) = xy1
    (x1,y1) = [xy for xy in intersect((d,e,f), (A,B,C)) \
    if abs((xy[0] - xy1[0]) * (xy[1] - xy1[1])) > .1][0]

n = i

print('Solution to problem 144 is %i.'%n)
    
    