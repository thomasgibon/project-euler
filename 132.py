# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:47:54 2015

@author: gibon
"""

import sympy

ones_list = [int('1'*r) for r in range(1,30)]
fact_list = [list(sympy.factorint(repunit).keys()) for repunit in ones_list]

