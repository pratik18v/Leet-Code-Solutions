#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:01:30 2017

@author: pratik18v
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in nums[i+1:]:
            idx = nums[i+1:].index(rem) + i + 1
            break
            
    return [i,idx]


if __name__ == '__main__':
    
    ans = twoSum([3,3],6)
    print ans