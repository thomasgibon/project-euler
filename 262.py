# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:16:39 2021

@author: Gibon
"""

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
import numpy as np
import sympy
from scipy.optimize import fsolve
from scipy.signal import argrelmin

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


H=lambda x,y: ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * np.exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )

X = np.arange(0, 1600, 1)
Y = np.arange(0, 1600, 1)
X, Y = np.meshgrid(X, Y)
Z = H(X,Y)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

a=H(200,200)
b=H(1400,1400)
ax.scatter(200,200,a,s=10)
ax.scatter(1400,1400,b,s=10)
ax.contour(X, Y, Z, 10, cmap="coolwarm_r", linestyles="solid")

x,y=sympy.symbols('x y', real=True)
h=( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * sympy.exp( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )

dhy1 = sympy.lambdify(y, sympy.diff(h.subs(x,0),y), modules=['numpy'])
dhy2 = sympy.lambdify(y, sympy.diff(h.subs(x,1600),y), modules=['numpy'])

x_max=fsolve(dhy1, 800)[0]
y_max=fsolve(dhy2, 800)[0]

f_min = max(H(x_max,0), H(y_max,1600))

