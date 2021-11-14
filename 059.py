# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:36:46 2015

@author: gibon
"""

import urllib
import string
from operator import xor

ascii_codes = range(ord('a'),ord('z') + 1)
ascii_printable = tuple(map(ord,string.printable))

file_url = "https://projecteuler.net/project/resources/p059_cipher.txt"
code = tuple(map(int,urllib.request.urlopen(file_url).read().decode('utf-8').split(',')))

the = (tuple(map(ord,'the')),tuple(map(ord,'The')))
n_thes_max = 0

l = len(code)
key_list  = []

for a in ascii_codes:
    for b in ascii_codes:
        for c in ascii_codes:
            key = (a,b,c)
            mask    = key * int(l/3) + key[0:l%3] # mask
            decrypt = tuple(map(xor,mask,code))   # result
            n_thes  = sum(decrypt[i:i+3] in the for i in range(len(decrypt))) # number of "the"s
           
            good_chars = sum(d in ascii_printable for d in decrypt)
            
            if n_thes > n_thes_max:
                print(n_thes)
                n_thes_max = n_thes
                good_key = ''.join(map(chr,key))
                original_ascii = decrypt
                original = ''.join(map(chr,original_ascii))

n = sum(original_ascii)

print('Solution to problem 87 is %i.'%n)

"""
Possibility to reduce the amount of letters to chose from
"""
key_options = [[],[],[]]

for i in range(3):
    for a in ascii_codes:
        if set([a ^ code[j] for j in range(i,l,3)]) < set(ascii_printable):
            key_options[i].append(a)

for a in key_options[0]:
    for b in key_options[1]:
        for c in key_options[2]:
            key = (a,b,c)
            mask    = key * int(l/3) + key[0:l%3] # mask
            decrypt = tuple(map(xor,mask,code))   # result
            n_thes  = sum(decrypt[i:i+3] in the for i in range(len(decrypt))) # number of "the"s
           
            good_chars = sum(d in ascii_printable for d in decrypt)
            
            if n_thes > n_thes_max:
                print(n_thes)
                n_thes_max = n_thes
                good_key = ''.join(map(chr,key))
                original_ascii = decrypt
                original = ''.join(map(chr,original_ascii))