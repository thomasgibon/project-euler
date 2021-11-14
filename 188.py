# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:00:12 2015

@author: gibon
"""

a = 1
i = 1

for i in range(100):
    if a > 1e10:
        a = int(str(a)[-10:]) * 1777
    else:
        a *= 1777
    print(str(a)[-8:])