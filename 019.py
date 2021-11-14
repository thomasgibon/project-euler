# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:36:05 2015

@author: gibon
"""

import datetime

count = 0

for year in range(1901,2001):
    for month in range(1,13):
        if datetime.datetime.weekday(datetime.date(year,month,1)) == 6:
            count += 1

n = count

print('Solution to problem 19 is %i.'%n)