#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: swp
@file: 2.py
@time:   2020/12/28
@version:  
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = ListNode(None)
        carray = 0
        while l1 or l2 or carray:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carray += v1 + v2
            tail.next = ListNode(None)
            tail.next.val = carray % 10
            carray //= 10
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next




