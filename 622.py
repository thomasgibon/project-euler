# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:14:31 2019

@author: gibon
"""

from sympy.ntheory import divisors

def shuffle(deck):
    
    n = len(deck)
    assert n%2==0 # only even numbers are accepted
    half = int(n/2)
    return tuple([card for cards in zip(deck[:half], deck[half:]) for card in cards])

def s(n):
    
    deck = tuple(range(n))
    
    c = 1
    new_deck = shuffle(deck)
    
    while new_deck != deck:
        c += 1
        new_deck = shuffle(new_deck)
    return c

test = [(i,s(i)) for i in range(0,100,2)]


def all_decks_n_shuffles(s):
    
    k = 2**s - 1
    divs = divisors(k)
    half = int(len(divs)/2)
    return [d+1 for d in divs[half:]]
    
test = [(i,all_decks_n_shuffles(i)) for i in range(0,8)]

answer = sum(all_decks_n_shuffles(60))