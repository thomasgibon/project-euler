# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:35:57 2015

@author: gibon
"""

import re
import string

def triangle(n):
    """Triangle number n"""
    return n * (n + 1.) / 2.

f = open('p042_words.txt','r')
l = [line for line in f.readlines()]

words = re.split('","|"',l[0])
words = [w for w in words if w != '']

alph = string.ascii_uppercase

word_value = [sum([alph.index(letter) + 1 for letter in word]) for word in words]

i = 1
t = [int(triangle(1))]

while t[-1] < max(word_value):
    i += 1
    t.append(int(triangle(i)))

n = sum([value in set(t) for value in word_value])

print('Solution to problem 27 is %i.'%n)