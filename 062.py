# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 00:22:42 2015

@author: gibon
"""

from collections import Counter

digs = 12

lb = int(10**((digs-1)/3))
ub = int(10**(digs/3)) + 1
cubes = set(str(k*k*k) for k in range(lb,ub))

cubes_sorted = [tuple(sorted(str(k*k*k))) for k in range(lb,ub)]
count = [(k,v) for k,v in Counter(cubes_sorted).items() if v == 5]
cube_list = [cube_list[0] for cube_list in count]

# Retrieve
sols = [[i + lb for i, k in enumerate(cubes_sorted) if k == c] for c in cube_list]

print(sols)





#for cube in cubes:
#    if int(cube) % 1000 == 0:
#        print(cube)
#    match = set(''.join(d) for d in itertools.permutations(cube)) & cubes
#    if len(match) > 1:
#        print(match)
#
#n = int(cube)