# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:06:08 2015

@author: gibon
"""

import urllib
import networkx as nx

file_url = 'https://projecteuler.net/project/resources/p079_keylog.txt'
keylog_text = urllib.request.urlopen(file_url).read().decode('utf-8').split()

keys = set(keylog_text)
#
#codes = []
#
#for key in keys:
#    for code in codes:
#        match = [(d,code.index(d)) for d in key if d in code]
#        new   = set(key) - set(code)
#        for d in code:
#            if d in key:
#                key.index(d)

G = nx.DiGraph()

for key in keys:
    G.add_edge(key[0], key[1])
    G.add_edge(key[1], key[2])

n = int(''.join(nx.topological_sort(G)))