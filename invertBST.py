#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:57:33 2016

QUESTION
--------
Invert a binary tree

@author: pratik18v
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root is not None):
            root.left, root.right = self.invertTree(root.right), \
                                    self.invertTree(root.left)
        
        return root
        
        
if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print 'The original tree\n'
    print '       {}       '.format(root.val)
    print '   {}-------{}   '.format(root.left.val,root.right.val)
    print ' {}--{}    {}--{}  \n'.format(root.left.left.val,root.left.right.val,
                                root.right.left.val,root.right.right.val)
    sol = Solution()
    root = sol.invertTree(root)

    print 'The reversed tree\n'   
    print '       {}       '.format(root.val)
    print '   {}-------{}   '.format(root.left.val,root.right.val)
    print ' {}--{}    {}--{}  '.format(root.left.left.val,root.left.right.val,
                                root.right.left.val,root.right.right.val)
    