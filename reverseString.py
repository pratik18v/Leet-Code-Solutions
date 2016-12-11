#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 04:06:01 2016

@author: pratik18v

QUESTION
--------
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        return r
        
        
        
if __name__ == '__main__':
    sol = Solution()
    org = "hello"
    rev = sol.reverseString(org)
    print "Original string is: {}\nReversed string is: {}".format(org,rev)