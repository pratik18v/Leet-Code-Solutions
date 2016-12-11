#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 15:53:33 2016

@author: pratik18v

QUESTION
--------

Calculate the sum of two integers a and b, but you are not allowed to use the 
operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        return sum([a,b])
        
if __name__ == '__main__':
    sol = Solution()
    a = 2
    b = 1
    ans = sol.getSum(a,b)
    print 'The sum of {} and {} is: {}'.format(a,b,ans)