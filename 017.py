# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:58:54 2015

@author: gibon
"""

import inflect
n = 0

for i in range(1,1001):
    words = inflect.engine().number_to_words(i)
    words = words.replace(' ','').replace('-','')
    n += len(words)

print('Solution to problem 17 is %i.'%n)