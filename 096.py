# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:03:51 2015

@author: gibon
"""

import urllib
import numpy as np
import time

file_url = 'https://projecteuler.net/project/resources/p096_sudoku.txt'
grid_raw = urllib.request.urlopen(file_url).read().decode('utf-8').split()

grids   = []
n_grids = len(grid_raw)

for i in range(2,n_grids,11):
    grids.append(np.array([[int(d) for d in list(row)] for row in grid_raw[i:i+9]]))

# each number belongs to a box, a row, a column
# find for each the possibilities from that

def row(i,grid):
    return set(range(10)) - set(grid[i,:])

def col(j,grid):
    return set(range(10)) - set(grid[:,j])

def box(i,j,grid):
    return set(range(10)) - set(grid[3*(i//3):3*(i//3+1),3*(j//3):3*(j//3+1)].flat)    

def options(grid):
    opts = [[set() for x in range(9)] for y in range(9)]
    for i,j in np.array(np.where(grid == 0)).T:
        opts[i][j] = row(i,grid) & col(j,grid) & box(i,j,grid)
    return np.array(opts)

def cell_solve(grid):
    
    ii,jj   = np.where(grid == 0)
    n_zeros = len(ii)
    
    while n_zeros > 0:
        for i,j in zip(ii,jj):
            opts = row(i,grid)&col(j,grid)&box(i,j,grid)
            if len(opts) == 1:
                grid[i,j] = opts.pop()
        ii,jj = np.where(grid == 0)
        if n_zeros == len(ii):
            raise Exception("Unsolvable, no cell has a single option.")
        n_zeros = len(ii)
    return grid

def solve(grid):
    """ Solves and returns a sudoku grid """
    
    ii,jj   = np.where(grid == 0)   # Indices of zeros in the grid
    n_zeros = len(ii)               # Number of zeros
    
    while n_zeros > 0:              # While there are zeros...
        for i,j in zip(ii,jj):      # Loop over zeros' indices
            
            opts = options(grid)    # Array of options (sets)
            
            o_row = set().union(*np.delete(opts[i,:],j)) # Options in the row (excluding the zero)
            
            o_col = set().union(*np.delete(opts[:,j],i)) # Options in the column (excluding the zero)
            
            o_box_a = np.copy(opts[3*(i//3):3*(i//3+1),3*(j//3):3*(j//3+1)])
            o_box_a[i%3,j%3] = set()
            o_box = set().union(*o_box_a.flatten()) # Options in the box (excluding the zero)
            
            o = opts[i,j]                           # Options in the cell (the zero)
            
            if len(o) == 1: # If only one option, then that's it
                print(i,j,'single',o)
                grid[i,j] = o.pop()
                opts[i,j] = set()                
            elif len(o - o_row) == 1:
                s = o - o_row
                grid[i,j] = s.pop()
                print(i,j,'row',o,o_row,o - o_row)
                opts[i,j] = set()
            elif len(o - o_col) == 1:
                s = o - o_col
                grid[i,j] = s.pop()
                print(i,j,'col',o,o_col,o - o_col) 
                opts[i,j] = set()
            elif len(o - o_box) == 1:
                s = o - o_box
                grid[i,j] = s.pop()
                print(i,j,'box',o,o_box,o - o_box) 
                opts[i,j] = set()
                
        ii,jj = np.where(grid == 0)
        n_zeros = len(ii)
        
    return grid
    
#%%
if __name__ == "__main__":
    
    i = 0
    s = 0
    
    start_time = time.time()
    
    for grid in grids:
        i += 1
        start_time = time.time()
        s += np.dot(solve(grid)[0,0:3],[100,10,1])
        print("Grille {0} : {1:.3f} seconds".format(i,time.time() - start_time))