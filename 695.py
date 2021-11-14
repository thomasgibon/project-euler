# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:57:15 2020

@author: Gibon

voir ici https://fr.wikipedia.org/wiki/Statistique_d%27ordre#Densit%C3%A9_d'une_statistique_d'ordre
"""

import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import sympy as sy
from mpl_toolkits.mplot3d import Axes3D
from itertools import combinations
from random import random

def areas_from_points(points=[(.2,.8),
                              (.6,.2),
                              (.8,.9)]):
    '''
    Provides the areas of rectangles created
    from the list of points.
    '''
    areas = []
    
    for pair in combinations(points,2):
        area = abs((pair[0][0] - pair[1][0]) * (pair[0][1] - pair[1][1]))
        areas.append(area)
        
    return areas

list_areas = []
    
for i in range(300000):
    
    if i%100000 == 0:
        print(i)
    
#    points=[(0.,
#             random()),
#            (random(),
#             0),
#            (1.,
#             1.)]
            
    points=[(0,
             0),
            (random(),
             random()),
             (1,
             1)]
            
    area = sorted(areas_from_points(points))
    
    list_areas.append(area)



areas_df = pd.DataFrame(list_areas)

areas_df.hist(sharex=True, sharey=True, bins=100, figsize=(16,9))
areas_df.mean()
# 0.10176904175057679
# 0.10160294452650558
# 0.10166836632899429
# 0.10158310747698737
# 0.10179597333696962
# 0.10178421742401667

    
# 2 points
# 0    0.111111 = 1/9

# 3 points
# 0    0.026846
# 1    0.102350 <- value to find
# 2    0.204890

# 4 points
# 0    0.011183
# 1    0.032308
# 2    0.063067
# 3    0.108919
# 4    0.177586
# 5    0.273647

# 5 points
# 0    0.005931
# 1    0.015493
# 2    0.028075
# 3    0.043935
# 4    0.066335
# 5    0.090836
# 6    0.126898
# 7    0.170929
# 8    0.235684
# 9    0.326876

list_areas = []

for i in range(100000):
    X = (random(),random(),random())
    Y = (random(),random(),random())
    area = (max(X)-min(X)) * (max(Y)-min(Y))

    list_areas.append(area)
    
areas_df = pd.DataFrame(list_areas)

areas_df.hist(sharex=True, sharey=True, bins=100, figsize=(16,9))
areas_df.mean()

# If we consider the smallest rectangle containing the three points
# we get a new coordinate system (O,(0,1),(1,0)) where we can figure out
# which rectangle gets first, second, or third depending on the last
# remaining point x,y in the new rectangle.

# This would help
# https://mathoverflow.net/questions/1294/mean-minimum-distance-for-n-random-points-on-a-one-dimensional-line

# in this new system, our rectangle areas become
# A1 = xy  (the bottom-left one)
# A2 = 1-y (the one on top)
# A3 = 1-x (the one on the right)

# "isosize" lines between pairs in {A1, A2, A3} are defined as

y0 = [x/1000 for x in range(1000)]
y1 = [pd.np.nan]*500 + [1/(x/1000)-1 for x in range(500,1000)]
y2 = [1/(x/1000+1) for x in range(1000)]

isosizes = pd.DataFrame([y0,y1,y2], columns = y0).T
plot = isosizes.plot()
plot.axis('equal')

# Considering the lower right area (under x = y)

phi = (5**.5 + 1)/2

# The 0-to-1 area is ln(phi) - 1 + phi/2
a0 = pd.np.log(phi) - 1 + phi/2
a5 = a0

# The 1-to-2 area is ln(2/(phi+1)) - phi + 2
a1 = pd.np.log(2/(phi+1)) - phi + 2
a4 = a1

# The 2-to-0 area is (phi-1)/2 - ln(2/phi)
a2 = (phi-1)/2 - pd.np.log(2/phi)
a3 = a2

plot = isosizes.plot()
plot.axis('equal')
plot.text(.6,.2,'a0 = {:.2f}'.format(a0))
plot.text(.9,.3,'a1 = {:.2f}'.format(a1))
plot.text(.9,.7,'a2 = {:.2f}'.format(a2))
plot.text(.6,.8,'a3 = {:.2f}'.format(a3))
plot.text(.4,.8,'a4 = {:.2f}'.format(a4))
plot.text(.2,.5,'a5 = {:.2f}'.format(a5))

# a1+a2+a0 should equal 1/2

# The second-largest rectangles happen as such

plot = isosizes.plot()
plot.axis('equal')
plot.text(phi-1,.2,'A3 = 1-x')
plot.text(.2,.5,'A2 = 1-y')
plot.text(.9,.3,'A1 = xy')
plot.text(.4,.8,'A1 = xy')
plot.text(phi-1,.8,'A3 = 1-x')
plot.text(.9,.7,'A2 = 1-y')

# CAREFUL: THIS IS ONLY 24/36 CASES
# 12/36 CASES when x,y,z are well-ordered

# Which gives the following expected value for the second
# biggest rectangle's area

# a0*A3 + a1*A1 + a2*A2 + a0*A2 + a1*A1 + a2*A3 =
# a0*(2-x-y) + 2*a1*x*y + a2*(2-x-y) =
# (a0+a2)*(2-x-y) + 2*a1*x*y
# (1-a1)*(2-x-y) + 2*a1*x*y

X,Y = pd.np.meshgrid(pd.np.linspace(0,1,1001),pd.np.linspace(0,1,1001))

Z1 = X*Y
Z2 = 1-Y
Z3 = 1-X

Z = xr.DataArray([Z1,Z2,Z3])

Zmed = pd.np.copy(Z1)
Zmax = pd.np.copy(Z1)
Zmin = pd.np.copy(Z1)

for x,_ in enumerate(X):
    for y,_ in enumerate(Y):
        if Z1[x,y]>=Z2[x,y]>=Z3[x,y] or Z3[x,y]>=Z2[x,y]>=Z1[x,y]:
            Zmed[x,y] = Z2[x,y]
        elif Z1[x,y]>=Z3[x,y]>=Z2[x,y] or Z2[x,y]>=Z3[x,y]>=Z1[x,y]:
            Zmed[x,y] = Z3[x,y]
        Zmax[x,y] = max(Z1[x,y],Z2[x,y],Z3[x,y])
        Zmin[x,y] = min(Z1[x,y],Z2[x,y],Z3[x,y])

fig = plt.figure()
ax = fig.gca(projection='3d')
surf1 = ax.plot_surface(X, Y, Zmed, linewidth=0, antialiased=False)
#surf2 = ax.plot_surface(X, Y, Zmin, linewidth=0, antialiased=False)
#surf3 = ax.plot_surface(X, Y, Zmax, linewidth=0, antialiased=False)

# Now what's the average x and y in each of a0, a1, a2?

# Let's try to solve it exactly
x, y = sy.symbols('x y')

phi1 = (sy.sqrt(5)-1)/2

a0w = sy.integrate(sy.integrate(1-x,(y,       0,       x)), (x,    0, phi1)) + \
      sy.integrate(sy.integrate(1-x,(y,       0,   1/x-1)), (x, phi1,    1))
      
a1w = sy.integrate(sy.integrate(x*y,(y,   1/x-1, 1/(x+1))), (x, phi1,    1))

a2w = sy.integrate(sy.integrate(1-y,(y, 1/(x+1),       x)), (x, phi1,    1))

# times 2 because of symmetry
A4 = 2*(a0w+a1w+a2w)

# The two other cases
# Average area of the second rectangle is 5/12
a3w = sy.integrate(sy.integrate(x*y,(y,1-x,1)),(x,0,1))

# times 2 because of symmetry
A2 = 2*a3w

# The answer is
sy.N((24*A4+12*A2)/36/4,10)
