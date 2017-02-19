#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 01:22:54 2017

@author: pratik18v
"""

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        else:    
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1