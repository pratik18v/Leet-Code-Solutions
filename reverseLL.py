#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 01:22:54 2017

@author: pratik18v
"""

class Solution(object):
    def reverseList(self, node, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not node:
            return None
            
        if not node.next:
            node.next = prev
            return node
    
        head = self.reverseList(node.next, node)
        node.next = prev
        return head
