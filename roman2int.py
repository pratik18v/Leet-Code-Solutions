#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 00:01:49 2017

@author: pratik18v
"""

# 3476=MMMCDLXXVI

# Function to create a stack. It initializes size of stack as 0

s = "DCXXI"
symbols = ['I','V','X','L','C','D','M']
dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
roman = [x for x in s]
intgr = 0
while len(roman) > 1:

    curr_val = roman.pop()
    intgr += dic[curr_val]

    if symbols.index(curr_val) > symbols.index(roman[-1]):
        intgr -= dic[roman.pop()]

if len(roman) == 1:
    intgr += dic[roman[0]]

print intgr
