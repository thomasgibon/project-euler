# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:07:12 2015

@author: gibon
"""

from collections import Counter

f = open('p054_poker.txt','r')
l = [line for line in f.readlines()]

all_hands = [(h[:15].split(),h[15:].split()) for h in l]

order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
hands_order = ['high card','one pair','double pair','two pairs',
               'three of a kind','straight','flush','full house',
               'four of a kind','straight flush','royal flush']

def howhigh(hand):
    values = [card[0] for card in hand]
    suits  = [card[1] for card in hand]
    
    val_count = Counter(values).values()
    suit_count = Counter(suits).values()
    seq = sorted([order.index(v) for v in values])
    
    howhigh  = 'high card'
    highcard = order[max(seq)]
    
    if 2 in val_count:
        twos = [v == 2 for v in val_count]
        howhigh = 'one pair'
        highcard = order[max([order.index(v) * t for v,t in zip(Counter(values).keys(),twos)])]
        if sum([v == 2 for v in val_count]) == 2:
            howhigh = 'double pair'
            
    if 3 in val_count:
        threes = [v == 3 for v in val_count]
        howhigh = 'three of a kind'
        highcard = order[max([order.index(v) * t for v,t in zip(Counter(values).keys(),threes)])]
        if set(val_count) == {2,3}:
            howhigh = 'full house'
            
    if 5 in suit_count and howhigh != 'full house':
        howhigh = 'flush'
        
    if 4 in val_count:
        fours = [v == 3 for v in val_count]
        howhigh = 'four of a kind'
        highcard = order[max([order.index(v) * t for v,t in zip(Counter(values).keys(),fours)])]
    

            
    if seq == list(range(seq[0],seq[-1]+1)):
        howhigh = 'straight'
        if 5 in suit_count:
            howhigh = 'straight flush'
            if seq == order[-5:]:
                howhigh = 'royal flush'
        
    return howhigh, highcard, [order[i] for i in sorted([order.index(value) for value in values])][::-1]

def comparehands(hands):
    val1 = howhigh(hands[0])
    val2 = howhigh(hands[1])
    
    if hands_order.index(val1[0]) > hands_order.index(val2[0]):
        return 1
    elif hands_order.index(val1[0]) < hands_order.index(val2[0]):
        return 2
    else:
        if order.index(val1[1]) > order.index(val2[1]):
            return 1
        elif order.index(val1[1]) < order.index(val2[1]):
            return 2
        else:
            i = 0
            while order.index(val1[2][i]) == order.index(val2[2][i]):
                i += 1
                if i == 4:
                    return 'tie'
            if order.index(val1[2][i]) > order.index(val2[2][i]):
                return 1
            else:
                return 2

# test
[(hands,howhigh(hands[comparehands(hands)-1]),comparehands(hands)) for hands in all_hands if howhigh(hands[0])[0] == howhigh(hands[1])[0]]
[(howhigh(hands[0]),howhigh(hands[1]),comparehands(hands)) for hands in all_hands if howhigh(hands[0])[0] == howhigh(hands[1])[0]]
[comparehands(hands) for hands in all_hands]


sum([comparehands(hands) == 1 for hands in all_hands])