# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:42:11 2015

@author: gibon
"""

import numpy as np

val = 200
coins = [200,100,50,20,10,5,2,1]
combi = 0

for a in range(val, -1, -coins[0]):
    for b in range(a, -1, -coins[1]):
        for c in range(b, -1, -coins[2]):
            for d in range(c, -1, -coins[3]):
                for e in range(d, -1, -coins[4]):
                    for f in range(e, -1, -coins[5]):
                        for g in range(f, -1, -coins[6]):
                            combi += 1

# not really sure about this one
# http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
coins    = (1, 2, 5, 10, 20, 50, 100, 200)
combi    = [0] * (val + 1)
combi[0] = 1

for coin in coins:
    for i in range(coin,val + 1):
        combi[i] += combi[i-coin]

n = combi[-1]

print('Solution to problem 31 is %i.'%n)

# Variant from http://www.theguardian.com/science/2015/sep/14/alex-bellos-did-you-solve-it-rugby-points-puzzle

coins = (3, 5, 7)
val   = 0

for val in range(100):
    combi    = [0] * (val + 1)
    combi[0] = 1

    for coin in coins:
        for i in range(coin,val + 1):
            combi[i] += combi[i-coin]
    
    n = combi[-1]
    
    if n <= 3:
        score_max = val

print(score_max)