#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 01:23:24 2017

@author: pratik18v
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while slow and fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
                
        return False