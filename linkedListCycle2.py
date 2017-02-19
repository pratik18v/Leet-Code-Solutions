#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 03:20:23 2017

@author: pratik18v
"""

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                    
                return fast
        
        return None