#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Time: 2021-09-28 12:26 上午

Author: huayang

Subject: 深度优先搜索

链接：

题目描述：

    给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

    路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
    输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    输出：3
    解释：和等于 8 的路径有 3 条，如图所示。
示例 2：
    输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    输出：3

"""
import os
import json
import doctest

from typing import *
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:  # noqa
        """"""
        # return self.dfs_node(root, targetSum)
        return self.dfs_prefixSum(root, targetSum)

    def dfs_node(self, root, targetSum):  # noqa
        """ 解法1：双重 DFS（双重递归） """

        def dfs_root(root, targetSum):  # noqa
            """ 计算从根节点开始的路径数 """
            if root is None:
                return 0

            ans = 0
            if root.val == targetSum:
                ans += 1

            delta_sum = targetSum - root.val  # 差值

            # 继续遍历左右子树
            ans += dfs_root(root.left, delta_sum)
            ans += dfs_root(root.right, delta_sum)
            return ans

        if root is None:
            return 0

        # 双重递归
        ret = dfs_root(root, targetSum)
        # 把每个节点都当做根节点计算一遍
        ret += self.dfs_node(root.left, targetSum)
        ret += self.dfs_node(root.right, targetSum)
        return ret

    def dfs_prefixSum(self, root, targetSum):  # noqa
        """ 解法2：前缀和 + DFS """
        from collections import defaultdict

        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(root, cur):  # noqa
            if root is None:
                return 0

            ret = 0
            cur += root.val
            ret += prefix[cur - targetSum]

            prefix[cur] += 1
            ret += dfs(root.left, cur)
            ret += dfs(root.right, cur)
            prefix[cur] -= 1

            return ret

        return dfs(root, 0)


def _test():
    """"""
    doctest.testmod()


if __name__ == '__main__':
    """"""
    _test()
