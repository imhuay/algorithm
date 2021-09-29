#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Time: 2021-09-27 12:35 上午

Author: huayang

Subject: 递归 & 迭代

链接：[21. 合并两个有序链表 - 力扣（LeetCode）](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

题目描述：
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例1：
    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]
示例 2：
    输入：l1 = [], l2 = []
    输出：[]
示例 3：
    输入：l1 = [], l2 = [0]
    输出：[0]

"""
import os
import json

from typing import *
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # noqa
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  # noqa
        """"""
        # return self._iter(l1, l2)
        return self._recur(l1, l2)

    def _recur(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 递归 """
        if l1 is None:  # 尾递归 1
            return l2
        elif l2 is None:  # 尾递归 2
            return l1
        elif l1.val < l2.val:  # 选出头结点较小的一个，余下部分递归
            l1.next = self._recur(l1.next, l2)
            return l1
        else:
            l2.next = self._recur(l1, l2.next)
            return l2

    def _iter(self, l1: ListNode, l2: ListNode) -> ListNode:  # noqa
        """ 迭代 """
        head = ListNode(-1)  # 初始化

        pre = head
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        pre.next = l1 if l1 is not None else l2

        return head.next


def _test():
    """"""
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    """"""
    _test()
