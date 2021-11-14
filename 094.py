# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:05:16 2016

@author: gibon

help from
http://mathforum.org/library/drmath/view/73118.html
and
https://www.alpertron.com.ar/QUAD.HTM
"""

import numpy as np

def areas(a):
    '''
    Returns the areas of the two almost equilateral triangle with two sides of 
    length a (a, a, a-1) and (a, a, a+1)
    '''
    
    A = ((a + 1)/4 * ((3 * a + 1) * (a - 1))**.5,
         (a - 1)/4 * ((3 * a - 1) * (a + 1))**.5)
         
    return A
#
#def hauteurs(a):
#    
#    h = (1/2 * (3*a*a - 2*a - 1)**.5,
#         1/2 * (3*a*a + 2*a - 1)**.5)
#    
#    return h

def hauteurs(AMAX):
    
    '''
    Returns side, altitude and perimeter of solution triangles
    '''
    
    P  = np.array([[7,8],[6,7]],dtype='int64') # Parameters for the diophantine eq system
    Qp = np.array([[-2],[-2]],dtype='int64')   # Constants for the longer edge option
    Qm = - Qp                                  # Constants for the shorter edge option
    ap = np.array([[1],[0]],dtype='int64')     # Initial condition (a = 1, h = 0) longer
    am = np.array([[1],[1]],dtype='int64')     # Initial condition (a = 1, h = 1) shorter
    
    sols = []
    
    while ap[0] < AMAX:
        ap   = np.dot(P,ap) + Qp
        peri = 3 * ap + 1
        sol  = ap.T.tolist()[0]
        sol.append(peri[0,0])
        sols.append(sol)
        
    while am[0] < AMAX:
        am = np.dot(P,am) + Qm
        peri = 3 * am - 1
        sol  = am.T.tolist()[0]
        sol.append(peri[0,0])
        sols.append(sol)
    
    sols.sort()
    
    return sols[:-2]
    
if __name__ == '__main__':
    
    n = sum(h[2] for h in hauteurs(1000000000/3))