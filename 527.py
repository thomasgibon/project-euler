# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:54:09 2019

@author: Gibon
"""

from random import randint, randrange
import numpy as np

def B_stoch(n, tries=1000):
    '''
    Number of guesses expected to find a random integer on 1..n, with the standard binary search
    '''
    n_guesses = []
       
    for i in range(tries):
        
        t = randint(1,n)
        L = 1
        H = n
        
        g = int((L+H)/2)
        c = 1
        
        while g != t:
            
            if g < t:
                L = g+1
                g = int((L+H)/2)
                c += 1
                
            elif g > t:
                H = g-1
                g = int((L+H)/2)
                c += 1
                
        n_guesses.append(c)
        
    return n_guesses

#n_guesses = B_stoch(5,1000000);sum(n_guesses)/len(n_guesses)

def R_stoch(n, tries=1000):
    '''
    Number of guesses expected to find a random integer on 1..n, with the random binary search
    '''
    n_guesses = []
    
    for i in range(tries):
        
        t = randint(1,n)
        L = 1
        H = n
        
        g = randrange(L,H+1)
        c = 1
        
        while g != t:
           
            if g < t:
                L = g+1
                if L==H:
                    g = L
                else:
                    g = randrange(L,H+1)
                c += 1
                
            elif g > t:
                H = g-1
                if L==H:
                    g = H
                else:
                    g = randrange(L,H+1)
                c += 1
                
        n_guesses.append(c)
        
    return n_guesses

#n_guesses = R_stoch(50,10000);sum(n_guesses)/len(n_guesses)

'''
Drawing probability graphs, it seems that the expected amount of guesses for n is

    1 * 2**0/n + 2 * 2**1/n + 3 * 2**2/n + ... k * 2/n if n is odd
    1 * 2**0/n + 2 * 2**1/n + 3 * 2**2/n + ... k * 1/n if n is even

for each n:
    
    n  numerator
    
    1    1
    2    3
    3    5
    4    8
    5   11
    6   14
    7   17
    8   21
    
    addressed here https://www.mathpages.com/home/kmath023/kmath023.htm

'''

def B_all(n):
    
    numerators = [0]
    n_guesses = [0]
    
    for k in range(1, n+1):
        
        numerator = numerators[-1] + (int(np.log2(k))+1)
        
        numerators.append(numerator)
        n_guesses.append(numerator/k)
    
    return (n_guesses, numerators)


def B_gen(n):
    
    if n == 1:
        return 1
        
    else:
        k = 1
        s = 1
        
        while k < n:
            k += 1
            s += (int(np.log2(k))+1)
            
        return s
  
B_gen(10000)



def B(n):
    '''
    
    '''
    m = (int(np.log2(n))+1)
    return (1 - 2**(m+1) + (m+1)*(n+1))/n
    
#B_all(100000)

def H(n):
    gamma = 0.57721566490153286060651209008240243104215933593992
    return gamma + np.log(n) + 0.5/n - 1./(12*n**2) + 1./(120*n**4)

def R(n):
    '''
    '''
    return 1/n + 2/n + 2*(1+1/n)*(H(n) - 1 - 1/2)

