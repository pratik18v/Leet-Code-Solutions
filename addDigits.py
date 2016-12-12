#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:18:33 2016

QUESTION
--------
Given a non-negative integer num, repeatedly add all its digits until the 
result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only 
one digit, return it.

@author: pratik18v
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = lambda num: int(reduce(lambda x,y: x+y, [int(i) for i in str(num)]))
        
        if len(str(num))>1:
            num = self.addDigits(s(num))
            #print num

        return num
        
if __name__ == '__main__':
    num = 999
    sol = Solution()
    ans = sol.addDigits(num)
    print 'The sum of digits is: {}'.format(ans)