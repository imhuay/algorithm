#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Time: 2021-09-26 12:45 上午

Author: huayang

Subject: 哈希表

链接：[1. 两数之和 - 力扣（LeetCode）](https://leetcode-cn.com/problems/two-sum/)

题目描述：
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
    
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    
    你可以按任意顺序返回答案。

示例 1：
    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
    输入：nums = [3,2,4], target = 6
    输出：[1,2]
示例 3：
    输入：nums = [3,3], target = 6
    输出：[0,1]

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # noqa
        """"""
        tmp = dict()

        for i in range(len(nums)):
            left = target - nums[i]  # 减去当前值
            if left in tmp:  # 如果差值在哈希表中，说明找到了答案
                return [tmp[left], i]

            tmp[nums[i]] = i  # 保存当前值的位置

        return []


def _test():
    """"""
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    """"""
    _test()
