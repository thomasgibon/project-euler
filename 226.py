#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:09:51 2019

@author: thomas
"""

import numpy as np

def s(x):
    
    return np.abs(np.round(x) - x)

def blancmange(fr=0, to=1, order=6):
    
    x = np.linspace(fr,to,2**order+1) #set max to .5, there is symmetry...
    y = np.zeros_like(x)
    
    for p in range(order):
        y += s(2**p*x)*2**-p
        
    return x,y

x,y = blancmange(fr=0.07890,
                 to=0.07891,
                 order=23) # that should be sufficient

# find the intersection between the circle and the curve
y_circle = 1./2 - (1./4**2 - (x - 1./4)**2)**.5

area_all = y - y_circle

intersect = x[area_all>=0][0]

# it seems the intersection is at 0.078907798222

area = area_all[area_all>=0]

# the integral can be calculated by recursion
# I(1) = 1/2
# I(x) = I(2x)/4+x**2/2 for 0<x<1/2

x,y = blancmange(fr=intersect,
                 to=0.5,
                 order=27) # that should be sufficient

y_circle = 1./2 - (1./4**2 - (x - 1./4)**2)**.5

area_all = y - y_circle
area = area_all[area_all>=0]
solution = area.sum()*(.5-intersect)/len(area)
