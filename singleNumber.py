#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 05:09:16 2016

@author: pratik18v

QUESTION
--------
Given an array of integers, every element appears twice except for one. Find 
that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it 
without using extra memory?
"""
from functools import reduce
import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        return reduce(operator.xor, nums)
        
if __name__ == '__main__':
    sol = Solution()
    arr = [-1]
    ans = sol.singleNumber(arr)
    print 'Single number in list is: {}'.format(ans)
    