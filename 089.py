# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:56:05 2016

@author: gibon
"""

from itertools import groupby
import bisect
import urllib

def roman2dec(s):
    ''' Returns a roman numeral, if valid according to the following:
    
    - Numerals must be arranged in descending order of size.
    - M, C, and X cannot be equalled or exceeded by smaller denominations.
    - D, L, and V can each only appear once.
    - Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
        - I can only be placed before V and X.
        - X can only be placed before L and C.
        - C can only be placed before D and M.
    
    '''
    
    digits = 'IVXLCDM'
    values = [1, 5, 10, 50, 100, 500, 1000]
    once   = 'DLV' # Can only appear once

    conv   = dict((d,v) for d,v in zip(digits,values))
    
    subtr  = ['IV','IX','XL','XC','CD','CM']
    
    for sub in subtr:
        conv[sub] = conv[sub[1]] - conv[sub[0]]
    
    value = 0
    
    if not all([d in digits for d in s]):
        raise SyntaxError('Some digits are not recognized as numbers!')
    
    if not all([len(list(g)) < 10 if k is not 'M' else True for k, g in groupby(s)]):
        raise SyntaxError('There are 10 or more digits in a row.')
    
    if not all([s.count(d) <= 1 for d in s if d in once]):
        raise SyntaxError('Either D, L, or V appear more than once...')
    
    i = 0
    
    while i < len(s):
        if (i <= len(s) - 2) & (s[i:i + 2] in subtr):
            if (i > 0) and (digits.index(s[i + 1]) > digits.index(s[i - 1])):
                raise SyntaxError('The digit you are subtracting from ({}) is higher than the one preceding the subtraction ({}).'
                .format(s[i + 1], s[i - 1]))
            value += conv[s[i:i + 2]]
            i += 2
        elif i == len(s) - 1:
            value += conv[s[i]]
            i += 1
        elif digits.index(s[i]) >= digits.index(s[i + 1]):
            value += conv[s[i]]
            i += 1
        else:
            if (i > 0) and (digits.index(s[i + 1]) > digits.index(s[i - 1])):
                raise SyntaxError('The digit you are subtracting from ({}) is higher than the one preceding the subtraction ({}).'
                .format(s[i + 1], s[i - 1]))
            value += conv[s[i:i + 2]]
            i += 2
    
    return value

def dec2roman(n):
    '''Converts a number to roman numerals'''
    
    digits = 'IVXLCDM'
    values = [1, 5, 10, 50, 100, 500, 1000]

    r2c = dict((d,v) for d,v in zip(digits,values))
    
    subtr  = ['IV','IX','XL','XC','CD','CM']
    
    roman = ''
    
    for sub in subtr:
        r2c[sub] = r2c[sub[1]] - r2c[sub[0]]
    
    c2r  = dict((v,k) for k,v in r2c.items())
    vals = list(sorted(c2r.keys()))
    
    while n > 0:
        i = bisect.bisect(vals,n)
        v = vals[i - 1]
        n -= v
        roman += c2r[v]
        
    return roman

def simplify_roman(s):
    return dec2roman(roman2dec(s))
    
if __name__ == '__main__':
    
    romans = urllib.request.urlopen('https://projecteuler.net/project/resources/p089_roman.txt')
    romans = [line.decode('utf-8').strip() for line in romans.readlines()]
    
    l = [len(r) - len(simplify_roman(r)) for r in romans]
    
    n = sum(l)