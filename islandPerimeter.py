#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:50:06 2016

@author: pratik18v

QUESTION
--------
You are given a map in form of a two-dimensional integer grid where 1 
represents land and 0 represents water. Grid cells are connected horizontally/
vertically (not diagonally). The grid is completely surrounded by water, and 
there is exactly one island (i.e., one or more connected land cells). The 
island doesn't have "lakes" (water inside that isn't connected to the water 
around the island). One cell is a square with side length 1. The grid is 
rectangular, width and height don't exceed 100. Determine the perimeter of the
island.
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        X = len(grid[0])
        Y = len(grid)
        
        neighbors = lambda x,y: [(i,j) for i in range(x-1,x+2)
                        for j in range(y-1,y+2)
                            if 0<=x<X 
                            and 0<=y<Y 
                            and (i != x or j != y)
                            and (i == x or j == y)
                            and 0<=i<X
                            and 0<=j<Y
                            and grid[j][i] == 1]
                                
        land = lambda g: [(iy,ix) for ix, row in enumerate(grid) for iy, i in 
                          enumerate(row) if i == 1]
        
        
        p = 0
        land_cells = land(grid)
        for l in land_cells:
            p = p+(4-len(neighbors(*l))) 
                
        return p
        
if __name__ == '__main__':
    sol = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    perimeter = sol.islandPerimeter(grid)
    print "The perimeter of the island is: {}".format(perimeter)