#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:50:06 2016

@author: pratik18v
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