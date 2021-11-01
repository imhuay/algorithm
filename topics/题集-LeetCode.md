# LeetCode

[Problems Index](#problems-index)

<!-- Tag: LeetCode -->

Problems Index
---
- [三数之和 (LeetCode, No.0015, 中等, 2021-10)](#三数之和-leetcode-no0015-中等-2021-10)
- [下一个更大元素 (LeetCode, No.0496, 简单, 2021-11)](#下一个更大元素-leetcode-no0496-简单-2021-11)
- [两数之和 (LeetCode, No.0001, 简单, 2021-10)](#两数之和-leetcode-no0001-简单-2021-10)
- [两数之和2(输入有序数组) (LeetCode, No.0167, 简单, 2021-10)](#两数之和2输入有序数组-leetcode-no0167-简单-2021-10)
- [两数相加 (LeetCode, No.0002, 中等, 2021-10)](#两数相加-leetcode-no0002-中等-2021-10)
- [两数相除 (LeetCode, No.0029, 中等, 2021-10)](#两数相除-leetcode-no0029-中等-2021-10)
- [二叉树的最大深度 (LeetCode, No.0104, 简单, 2021-10)](#二叉树的最大深度-leetcode-no0104-简单-2021-10)
- [二叉树的最小深度 (LeetCode, No.0111, 简单, 2021-10)](#二叉树的最小深度-leetcode-no0111-简单-2021-10)
- [分隔链表 (LeetCode, No.0086, 中等, 2021-10)](#分隔链表-leetcode-no0086-中等-2021-10)
- [合并两个有序链表 (LeetCode, No.0021, 简单, 2021-10)](#合并两个有序链表-leetcode-no0021-简单-2021-10)
- [字符串中的单词数 (LeetCode, No.0434, 简单, 2021-10)](#字符串中的单词数-leetcode-no0434-简单-2021-10)
- [将数据流变为多个不相交区间 (LeetCode, No.0352, 困难, 2021-10)](#将数据流变为多个不相交区间-leetcode-no0352-困难-2021-10)
- [排列硬币 (LeetCode, No.0441, 简单, 2021-10)](#排列硬币-leetcode-no0441-简单-2021-10)
- [接雨水 (LeetCode, No.0042, 困难, 2021-10)](#接雨水-leetcode-no0042-困难-2021-10)
- [搜索二维矩阵2 (LeetCode, No.0240, 中等, 2021-10)](#搜索二维矩阵2-leetcode-no0240-中等-2021-10)
- [搜索旋转排序数组 (LeetCode, No.0033, 中等, 2021-10)](#搜索旋转排序数组-leetcode-no0033-中等-2021-10)
- [最接近的三数之和 (LeetCode, No.0016, 中等, 2021-10)](#最接近的三数之和-leetcode-no0016-中等-2021-10)
- [最长回文子串 (LeetCode, No.0005, 中等, 2021-10)](#最长回文子串-leetcode-no0005-中等-2021-10)
- [有效三角形的个数 (LeetCode, No.0611, 中等, 2021-10)](#有效三角形的个数-leetcode-no0611-中等-2021-10)
- [盛最多水的容器 (LeetCode, No.0011, 中等, 2021-10)](#盛最多水的容器-leetcode-no0011-中等-2021-10)
- [路径总和3 (LeetCode, No.0437, 中等, 2021-10)](#路径总和3-leetcode-no0437-中等-2021-10)
- [重复的DNA序列 (LeetCode, No.0187, 中等, 2021-10)](#重复的dna序列-leetcode-no0187-中等-2021-10)

---

### 三数之和 (LeetCode, No.0015, 中等, 2021-10)


[![双指针(首尾)](https://img.shields.io/badge/双指针(首尾)-lightgray.svg)](技巧-双指针(滑动窗口).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 双指针(首尾) -->

<summary><b>问题简述</b></summary> 

```text
给定一个数组，找出该数组中所有和为 0 的三元组。
```

<summary><b>思路</b></summary>

- 排序后，问题可以简化成两数之和（LeetCode-167）；
- 先固定一个数，然后利用首尾双指针进行对向遍历；
- 注意跳过相同结果；


<details><summary><b>题目描述</b></summary> 

```text
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]

示例 2：
    输入：nums = []
    输出：[]

示例 3：
    输入：nums = [0]
    输出：[]

提示：
    0 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>Python</b></summary> 

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # assert
        ret = []
        L = len(nums)
        if L < 3:
            return ret

        # 设置目标值
        target = 0
        # 排序
        nums = sorted(nums)

        for i in range(L - 2):  # 固定第一个数
            # 剪枝
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] + nums[i + 1] + nums[i + 2] > target: break
            if nums[i] + nums[L - 2] + nums[L - 1] < target: continue

            # 设置左右指针
            l, r = i + 1, L - 1
            while l < r:

                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:  # s == target
                    ret.append([nums[i], nums[l], nums[r]])

                    # 同时移动双指针
                    l += 1
                    r -= 1

                    # 如果跟上一个值相同，就跳过
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1

        return ret

```

</details>

---
### 下一个更大元素 (LeetCode, No.0496, 简单, 2021-11)


[![单调栈](https://img.shields.io/badge/单调栈-lightgray.svg)](数据结构-栈(单调栈).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 单调栈 -->

<summary><b>问题简述</b></summary>

```txt
找出 nums1 中每个元素在 nums2 中的下一个比其大的值，不存在输出 -1；
其中 nums1 是 nums2 的子集。

本题实际上就是模拟了**单调栈**最常见的使用场景；
```

<details><summary><b>题目描述</b></summary>

```txt

给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中 nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例 1:
    输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
    输出: [-1,3,-1]
    解释:
        对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
        对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
        对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
示例 2:
    输入: nums1 = [2,4], nums2 = [1,2,3,4].
    输出: [3,-1]
    解释:
        对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
        对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
 
提示：
    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 10^4
    nums1和nums2中所有整数 互不相同
    nums1 中的所有整数同样出现在 nums2 中
 

进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>思路：单调栈（Python）</b></summary>

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}  # 保存结果
        stack = []  # 模拟单调栈
        for num in reversed(nums2):  # 逆序遍历
            while stack and num >= stack[-1]:  # 当栈不为空，且当前值大于栈顶值时
                stack.pop()  # 弹出栈顶值（list.pop 默认弹出最后一个值）
            res[num] = stack[-1] if stack else -1  # 如果此时栈不为空，那么栈顶值就是下一个比当前大的值
            stack.append(num)  # 把当前值入栈
        return [res[num] for num in nums1]  # 遍历完 nums2 中的所有元素后，就得到了 nums1 中每个元素下一个比它大的值，因为 num1 是 nums2 的子集
```

</details>

---
### 两数之和 (LeetCode, No.0001, 简单, 2021-10)


[![哈希表](https://img.shields.io/badge/哈希表-lightgray.svg)](技巧-哈希表.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 哈希表 -->

<summary><b>问题描述</b></summary>

```txt
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

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
 

提示：
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    只会存在一个有效答案

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```


<details><summary><b>Python3</b></summary>

```python
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

```

</details>

---
### 两数之和2(输入有序数组) (LeetCode, No.0167, 简单, 2021-10)


[![首尾双指针](https://img.shields.io/badge/首尾双指针-lightgray.svg)](技巧-双指针(滑动窗口).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 首尾双指针 -->

<summary><b>问题简述</b></summary>

```txt
找出一个非递减数组中和等于 target 的两个数字，输出它们的下标。

假定题目一定有一个解。
```

<details><summary><b>题目描述</b></summary>

```txt
给定一个已按照 非递减顺序排列 的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

 
示例 1：
    输入：numbers = [2,7,11,15], target = 9
    输出：[1,2]
    解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
示例 2：
    输入：numbers = [2,3,4], target = 6
    输出：[1,3]
示例 3：
    输入：numbers = [-1,0], target = -1
    输出：[1,2]


提示：
    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers 按 非递减顺序 排列
    -1000 <= target <= 1000
    仅存在一个有效答案

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>双指针（Python）</b></summary>

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """"""
        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            tmp = numbers[lo] + numbers[hi]

            if tmp < target:
                lo += 1
            elif tmp > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]
```

</details>

---
### 两数相加 (LeetCode, No.0002, 中等, 2021-10)


[![链表](https://img.shields.io/badge/链表-lightgray.svg)](数据结构-链表.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 链表 -->

<summary><b>问题描述</b></summary>

```txt
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例1：
    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.

示例2：
    输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    输出：[8,9,9,9,0,0,0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```


<details><summary><b>算法简述</b></summary>

```txt

```

</details>

<details><summary><b>代码</b></summary>

**python**
- 时间复杂度：`O()`，空间复杂度：`O()`
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # noqa
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:  # noqa
        """"""
        ret = p = ListNode()

        s = 0
        while l1 or l2 or s != 0:  # 注意遍历条件，当三个都不为真时才会结束
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)

            p.next = ListNode(s % 10)  # 个位
            p = p.next

            # 遍历链表
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            s = s // 10  # 进位

        return ret.next
```

</details>

<details><summary><b>备忘</b></summary>

1. 1
2. 2

</details>

---
### 两数相除 (LeetCode, No.0029, 中等, 2021-10)


[![位运算](https://img.shields.io/badge/位运算-lightgray.svg)](技巧-位运算.md)
[![二分查找](https://img.shields.io/badge/二分查找-lightgray.svg)](算法-二分查找.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 位运算、二分查找 -->

<summary><b>问题简述</b></summary>

```txt
不使用乘法、除法和 mod 运算符，返回两数相除的整数部分，如 10/3 返回 3。
```

<details><summary><b>题目描述</b></summary>

```txt
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3
    解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2
    解释: 7/-3 = truncate(-2.33333..) = -2

提示：
    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>思路：二分查找</b></summary>

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """"""
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # 按照题目要求，只有一种情况会溢出
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        # 核心操作
        def div(a, b):
            if a < b:
                return 0

            cnt = 1
            tb = b
            while (tb + tb) <= a:
                cnt += cnt
                tb += tb

            return cnt + div(a - tb, b)

        ret = div(abs(dividend), abs(divisor))
        return ret if sign else -ret
```

**核心操作说明**，以 60 / 8 为例：
```txt
第一轮 div(60, 8): 8 -> 32 时停止，因为 32 + 32 > 60，返回 4
第二轮 div(28, 8): 8 -> 16 时停止，因为 16 + 16 > 28，返回 2
第三轮 div(8, 8):  8 -> 8  时停止，因为 8  +  8 >  8，返回 1
第三轮 div(0, 8):  因为 0 < 8，返回 0

因此结果为 1 + 2 + 4 = 7
```

</details>

---
### 二叉树的最大深度 (LeetCode, No.0104, 简单, 2021-10)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-二叉树(树).md)
[![递归](https://img.shields.io/badge/递归-lightgray.svg)](算法-递归(迭代).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 二叉树，递归 -->

<summary><b>问题简述</b></summary>

```txt
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

示例：
    给定二叉树 [3,9,20,null,null,15,7]，
        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<summary><b>思路</b></summary>

- 递归：当前二叉树的最大深度等于**左右子树的最大深度** `+ 1`

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # 尾递归
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

</details>

---
### 二叉树的最小深度 (LeetCode, No.0111, 简单, 2021-10)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-二叉树(树).md)
[![DFS](https://img.shields.io/badge/DFS-lightgray.svg)](算法-深度优先搜索.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 二叉树，DFS -->

<summary><b>问题简述</b></summary>

```txt
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

示例：
    给定二叉树 [3,9,20,null,null,15,7]，
        3
       / \
      9  20
        /  \
       15   7
    返回它的最小深度 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<summary><b>思路</b></summary>

- 深度优先搜索，记录过程中的最小深度；

<details><summary><b>深度优先搜索（Python）</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """"""
        if not root:  # 尾递归1
            return 0

        if not root.left and not root.right:  # 尾递归 2 *
            return 1
        
        min_depth = 10**5 + 10
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        
        return min_depth + 1
```

</details>

---
### 分隔链表 (LeetCode, No.0086, 中等, 2021-10)


[![链表](https://img.shields.io/badge/链表-lightgray.svg)](数据结构-链表.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 链表 -->

<summary><b>问题描述</b></summary>

- 快排链表的核心操作；

```txt
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：
    输入：head = [1,4,3,2,5,2], x = 3
    输出：[1,2,2,4,3,5]
示例 2：
    输入：head = [2,1], x = 2
    输出：[1,2]
 
提示：
    链表中节点的数目在范围 [0, 200] 内
    -100 <= Node.val <= 100
    -200 <= x <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<div align="center"><img src="../_assets/partition.jpeg" height="150" /></div>


<details><summary><b>算法简述</b></summary>

```txt
新建两个链表，分别保存小于 x 和大于等于 x 的，最后拼接；
```

</details>

<details><summary><b>Python3</b></summary>

**python**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """"""
        # l/r 会进行移动，lo/hi 为头节点
        l = lo = ListNode(0)
        r = hi = ListNode(0)
        
        while head:
            if head.val < x:  # 小于 x 的拼到 lo
                l.next = head
                l = l.next
            else:  # 大于等于 x 的拼到 hi
                r.next = head
                r = r.next
                
            head = head.next
        
        # 因为不能保证最后遍历的节点在 hi 中，所以必须加上这一步，切断循坏
        r.next = None  # 关键步骤
        l.next = hi.next
        
        return lo.next
```

</details>

---
### 合并两个有序链表 (LeetCode, No.0021, 简单, 2021-10)


[![递归](https://img.shields.io/badge/递归-lightgray.svg)](算法-递归(迭代).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 递归 -->

<summary><b>问题描述</b></summary>

```txt
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：
    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]
示例 2：
    输入：l1 = [], l2 = []
    输出：[]
示例 3：
    输入：l1 = [], l2 = [0]
    输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```


<details><summary><b>递归（Python）</b></summary>

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # noqa
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  # noqa
        """ 递归 """
        if l1 is None:  # 尾递归 1
            return l2
        elif l2 is None:  # 尾递归 2
            return l1
        elif l1.val < l2.val:  # 选出头结点较小的一个，余下部分递归
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


```

</details>


<details><summary><b>迭代（Python）</b></summary>

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # noqa
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  # noqa
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

```

</details>

---
### 字符串中的单词数 (LeetCode, No.0434, 简单, 2021-10)


[![字符串](https://img.shields.io/badge/字符串-lightgray.svg)](数据结构-字符串.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 字符串 -->

<summary><b>问题描述</b></summary>

```txt
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:
    输入: "Hello, my name is John"
    输出: 5
    解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-segments-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```


<details><summary><b>Python3</b></summary>

```python
class Solution:
    def countSegments(self, s):
        
        # 针对第一个字符初始化，注意处理空串
        ans = 0 if s == '' or s[0] == ' ' else 1

        for i in range(1, len(s)):
            if s[i] != ' ' and s[i - 1] == ' ':
                ans += 1

        return ans

```

</details>

---
### 将数据流变为多个不相交区间 (LeetCode, No.0352, 困难, 2021-10)


[![二分查找](https://img.shields.io/badge/二分查找-lightgray.svg)](算法-二分查找.md)
[![模拟](https://img.shields.io/badge/模拟-lightgray.svg)](基础-模拟.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 二分查找、模拟 -->

<summary><b>问题简述</b></summary>

```txt
给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。

实现 SummaryRanges 类：
    SummaryRanges() 使用一个空数据流初始化对象。
    void addNum(int val) 向数据流中加入整数 val 。
    int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。

进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

**“进阶”**：在插入过程中完成合并操作；

<details><summary><b>示例</b></summary>

```txt
输入：
    ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
输出：
    [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

解释：
    SummaryRanges summaryRanges = new SummaryRanges();
    summaryRanges.addNum(1);      // arr = [1]
    summaryRanges.getIntervals(); // 返回 [[1, 1]]
    summaryRanges.addNum(3);      // arr = [1, 3]
    summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
    summaryRanges.addNum(7);      // arr = [1, 3, 7]
    summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
    summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
    summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
    summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]

提示：
    0 <= val <= 10^4
    最多调用 addNum 和 getIntervals 方法 3 * 10^4 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>思路1：暴力求解（Python）</b></summary>

- 每次 `getIntervals` 时，先对数组排序，然后依次找出每个不相交的区间；

```python
class SummaryRanges:

    def __init__(self):
        self.ls = []

    def addNum(self, val: int) -> None:
        """"""
        self.ls.append(val)

    def getIntervals(self) -> List[List[int]]:
        """"""
        ls = sorted(self.ls)
        ret = []
        l = ls[0]
        for i in range(1, len(ls)):
            if ls[i] - ls[i-1] > 1:  # 判断是否需要合并
                ret.append([l, ls[i-1]])
                l = ls[i]
        
        ret.append([l, ls[-1]])

        return ret
```

</details>


<details><summary><b>思路2：分情况讨论（模拟，Python）</b></summary>

- 明确每次 `addNum` 时，区间会发生那些变化：
    - 情况1：存在一个区间 `[l, r]` 满足 `l <= val <= r`；
    - 情况2：存在一个区间 `[l, r]` 满足 `r + 1 == val`；
    - 情况3：存在一个区间 `[l, r]` 满足 `l - 1 == val`；
    - 情况4：存在两个个区间 `[l0, r0]` 和 `[l1, r1]` 满足 `r0 + 1 == val == l1 - 1`，即加入 val 后，会合并为一个区间 `[l0, r1]`
    - 情况5：以上均不满足，加入后 val 单独成为一个区间；

- 这里使用了 `SortedDict` 降低了代码难度，也可以使用一个有序数组来模拟；

- 时间复杂度: `addNum O(NlgN)`、`getIntervals O(N)`；
- 空间复杂度: `O(N)`；


```python
from sortedcontainers import SortedDict
from bisect import bisect_right, bisect_left

class SummaryRanges:

    def __init__(self):
        self.ret = SortedDict()  # {l: r}
        # 加入首尾两个哨兵，防止区间不存在的情况，这样会徒增很多判断
        self.ret[-10] = -10
        self.ret[10010] = 10010

    def addNum(self, val: int) -> None:
        ret = self.ret
        L = list(self.ret.keys())
        R = list(self.ret.values())

        # 二分找出 val 的相邻区间
        idx = bisect_left(L, val)  # idx = ret.bisect_left(val)
        pre = L[idx - 1], R[idx - 1]
        nxt = L[idx], R[idx]

        if pre[0] <= val <= pre[1] or nxt[0] <= val <= nxt[1]:  # 情况1
            pass
        elif pre[1] + 1 == val == nxt[0] - 1:  # 情况4
            ret.pop(nxt[0])
            ret[pre[0]] = nxt[1]
        elif pre[1] + 1 == val:  # 情况2
            ret[pre[0]] = val
        elif nxt[0] - 1 == val:  # 情况3
            ret.pop(nxt[0])
            ret[val] = nxt[1]
        else:  # 情况5
            ret[val] = val

    def getIntervals(self) -> List[List[int]]:
        return list(self.ret.items())[1:-1]  # 去除两个哨兵
```

- 上面的代码中用到了 `SortedDict`，示例：

```python
>>> d = SortedDict()
>>> d[3] = 33
>>> d[2] = 22
>>> d[4] = 44
>>> d[6] = 66
>>> d[7] = 77
>>> d
SortedDict({2: 22, 3: 33, 4: 44, 6: 66, 7: 77})
>>> d.bisect_left(4)  # 二分查找返回的是插入位置
2
>>> d.bisect_right(4)  # left 和 right 的区别是如果插入值已存在，则 left 会插到前面，right 会插到后面
3
```

</details>

---
### 排列硬币 (LeetCode, No.0441, 简单, 2021-10)


[![二分查找](https://img.shields.io/badge/二分查找-lightgray.svg)](算法-二分查找.md)
[![数学](https://img.shields.io/badge/数学-lightgray.svg)](基础-数学.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 二分查找、数学 -->

<summary><b>问题简述</b></summary>

```txt
你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

示例 1：
    输入：n = 5
    输出：2
    解释：因为第三行不完整，所以返回 2 。

提示：
    1 <= n <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arranging-coins
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<div align="center"><img src="../_assets/arrangecoins1-grid.jpeg" height="150" /></div>


<details><summary><b>思路1：二分查找</b></summary>

- 因为时间复杂度为 `O(logN)`，所以直接在 `[1, n]` 的范围里找即可

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left

```

</details>


<details><summary><b>思路2：数学</b></summary>

- 解方程 $(1+x)*x/2 = n$；
- 去掉小于 0 的解，保留：$x=(-1+\sqrt{8n+1})/2$

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (8 * n + 1) ** 0.5) / 2)
```

</details>

---
### 接雨水 (LeetCode, No.0042, 困难, 2021-10)


[![双指针(首尾)](https://img.shields.io/badge/双指针(首尾)-lightgray.svg)](技巧-双指针(滑动窗口).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 双指针(首尾) -->

<summary><b>问题简述</b></summary>

```txt
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1（如图）：
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<div align="center"><img src="../_assets/rainwatertrap.png" height="150" /></div>


<details><summary><b>思路1：双指针(Python)</b></summary>

```Python
class Solution:
    def trap(self, height: List[int]) -> int:
        """"""
        l, r = 0, len(height) - 1
        
        ans = 0
        max_l = max_r = 0  # 保存当前位置时，左右最高的柱子
        
        while l <= r:
            if height[l] <= height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    ans += max_l - height[l]
                l += 1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    ans += max_r - height[r]
                r -= 1
                
        return ans
``` 

</details>


<details><summary><b>思路2：左右遍历两次(C++)</b></summary>

```C++
class Solution {
public:
    int trap(vector<int>& H) {
        int n = H.size();
        
        vector<int> l_max(H);
        vector<int> r_max(H);
        
        for(int i=1; i<n; i++)
            l_max[i] = max(l_max[i-1], l_max[i]);
        
        for(int i=n-2; i>=0; i--)
            r_max[i] = max(r_max[i+1], r_max[i]);
        
        int ret = 0;
        for (int i=1; i<n-1; i++)
            ret += min(l_max[i], r_max[i]) - H[i];
        
        return ret;
    }
};
``` 

</details>

---
### 搜索二维矩阵2 (LeetCode, No.0240, 中等, 2021-10)


[![二分](https://img.shields.io/badge/二分-lightgray.svg)](算法-二分查找.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 二分 -->

<summary><b>问题简述</b></summary>

```txt
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。
该矩阵具有以下特性：
    每行的元素从左到右升序排列。
    每列的元素从上到下升序排列。
```

<details><summary><b>题目描述</b></summary>

```txt
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

    每行的元素从左到右升序排列。
    每列的元素从上到下升序排列。

示例 1：
    输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
    输出：true
示例 2：
    输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
    输出：false

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -10^9 <= matrix[i][j] <= 10^9
    每行的所有元素从左到右升序排列
    每列的所有元素从上到下升序排列
    -10^9 <= target <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<div align="center"><img src="../_assets/searchgrid2.jpeg" height="300" /></div> 

</details>


<details><summary><b>思路1：二分查找（Python）</b></summary>

- 时间复杂度：`O(MlogN)`

```python
from bisect import bisect_left

# 直接层序二分搜索
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect_left(row, target)  # 注意这里要用 bisect_left
            if idx < len(row) and row[idx] == target:
                return True
        return False


# 稍微做一些优化
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False

        lo, hi = 0, n
        for row in matrix:
            idx = bisect_left(row, target, lo, hi)

            # 逐步缩小每层遍历的范围
            if idx < len(row):
                if row[idx] == target:
                    return True
                elif row[idx] < target:
                    lo = idx
                elif row[idx] > target:
                    hi = idx

        return False
```

</details>


<details><summary><b>思路2：模拟二分（Python）</b></summary>

- **二分搜索的核心**是将搜索区域分成两个部分，且这两个部分具有相反的性质，每次可以排除一半左右搜索区域；
- 对本题来说，如果从**右上角**开始遍历，则有：所有左边的值都比当前值小，所有下方的值都比当前值大；
- 时间复杂度：`O(M+N)`

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:  # 比当前值大，横向往左进一格
                j -= 1
            else:  # matrix[i][j] < target 比当前值小，纵向往下进一格
                i += 1
        return False
```

</details>

---
### 搜索旋转排序数组 (LeetCode, No.0033, 中等, 2021-10)


[![二分查找](https://img.shields.io/badge/二分查找-lightgray.svg)](算法-二分查找.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 二分查找 -->

<summary><b>问题简述</b></summary>

```txt
在一个旋转过的有序数组中搜索某值，若存在返回下标，否则返回 -1。
```

<summary><b>思路</b></summary>

- “二分”的本质是两段性，而不是单调性；即只要二分后，左边满足某个性质，右边不满足某个性质，即可使用二分；
- 比如本题二分后，有前半段满足 >= nums[0]，而后半段不满足；

    > [LogicStack-LeetCode/33.搜索旋转排序数组（中等）](https://github.com/SharingSource/LogicStack-LeetCode/blob/main/LeetCode/31-40/33.%20搜索旋转排序数组（中等）.md#二分解法)

<details><summary><b>题目描述</b></summary>

```txt
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

示例 1：
    输入：nums = [4,5,6,7,0,1,2], target = 0
    输出：4
示例 2：
    输入：nums = [4,5,6,7,0,1,2], target = 3
    输出：-1
示例 3：
    输入：nums = [1], target = 0
    输出：-1
 

提示：
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    nums 中的每个值都 独一无二
    题目数据保证 nums 在预先未知的某个下标上进行了旋转
    -10^4 <= target <= 10^4
 
进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>二分查找（Python）</b></summary>

- 将数组从中间分开成左右两部分时，一定有一部分的数组是有序的。

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        L = len(nums) - 1
        l, r = 0, L
        while l <= r:
            mid = l + (r - l) // 2  # 中点下标

            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:  # [0, mid) 是有序的
                # 如果目标在[0, mid)，则将搜索范围缩小到 [0,mid-1]，反之 [mid+1,L]
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # (mid, L] 是有序的
                # 同理，如果目标在(mid, L]，则将搜索范围缩小到 [mid+1,L]，反之 [0,mid-1]
                if nums[mid] < target <= nums[L]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

```

</details>

---
### 最接近的三数之和 (LeetCode, No.0016, 中等, 2021-10)


[![双指针(首尾)](https://img.shields.io/badge/双指针(首尾)-lightgray.svg)](技巧-双指针(滑动窗口).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 双指针(首尾) -->

<summary><b>问题简述</b></summary> 

```text
给定一个数组，找出该数组中和最接近指定值的三元组。
```

<summary><b>思路</b></summary> 

- 思路跟三数之和基本一致；
- 当找到比当前更接近的结果时更新；

<details><summary><b>题目描述</b></summary> 

```text
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
    输入：nums = [-1,2,1,-4], target = 1
    输出：2
    解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

提示：
    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<details><summary><b>Python</b></summary> 

```python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """"""
        nums = sorted(nums)

        L = len(nums)
        ret = nums[0] + nums[1] + nums[2]  # 初始化，len(nums) >= 3
        for i in range(L - 2):

            # 跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 利用单调性剪纸
            min_s = nums[i] + nums[i + 1] + nums[i + 2]  # 最小和
            if min_s > target:
                if abs(min_s - target) < abs(ret - target):
                    ret = min_s
                break

            max_s = nums[i] + nums[L - 2] + nums[L - 1]  # 最大和
            if max_s < target:
                ret = max_s
                continue

            # 初始化双指针
            l, r = i + 1, L - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(ret - target):
                    ret = s

                if s < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                elif s > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                else:  # ret == target
                    return ret
        return ret

```

</details>

<details><summary><b>利用单调性剪枝</b></summary> 

- 在经过排序后，每轮迭代时，三数之和的最大值和最小值是确定的；
- 所以如果最小值比目标值大，那么后面无论怎么移动双指针，差值都只会越来越大；最大值比目标值小时同理；
- 代码细节：

    ```python
    # 剪枝：利用单调性
    min_s = nums[i] + nums[i + 1] + nums[i + 2]  # 最小和
    if min_s > target:  # 如果最小和也大于 target，则剩余部分的差值肯定越来越大
        # 容易忽略的一步，注意此时也是有可能出现答案的，比如 ret < 0 < min_s 时
        if abs(min_s - target) < abs(ret - target):
            ret = min_s
        break

    max_s = nums[i] + nums[L - 2] + nums[L - 1]  # 最大和
    if max_s < target:  # 如果最大和也小于 target，则剩余部分的差值肯定越来越大
        ret = max_s  # 此时 ret < max_s < target，所以 max_s 必然比当前 ret 更接近目标值
        continue
    ```

</details>

---
### 最长回文子串 (LeetCode, No.0005, 中等, 2021-10)


[![DP](https://img.shields.io/badge/DP-lightgray.svg)](算法-动态规划.md)
[![模拟](https://img.shields.io/badge/模拟-lightgray.svg)](基础-模拟.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: DP、模拟 -->

<summary><b>问题简述</b></summary>

```txt
给你一个字符串 s，找到 s 中最长的回文子串。
```

<details><summary><b>题目描述</b></summary>

```txt
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。
示例 2：
    输入：s = "cbbd"
    输出："bb"
示例 3：
    输入：s = "a"
    输出："a"
示例 4：
    输入：s = "ac"
    输出："a"

提示：
    1 <= s.length <= 1000
    s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>思路1：动态规划（C++）</b></summary>

- 状态定义：`dp[i][j] := 子串 s[i:j] 是否为回文串`；
- 状态转移方程：`dp[i][j] := dp[i+1][j-1] == True 且 s[i] == s[j]`；
- 初始状态：`dp[i][j] := True` 当 `i == j` 或 `j == i + 1 && s[i] == s[j]` 

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();

        vector<vector<int>> dp(n, vector<int>(n, 0));
        int max_len = 1;    // 保存最长回文子串长度
        int start = 0;      // 保存最长回文子串起点

        // 初始状态1：子串长度为 1 时，显然是回文子串
        for (int i = 0; i < n; i++)
            dp[i][i] = 1;

        //for (int j = 1; j < n; j++)         // 子串结束位置
        //    for (int i = 0; i < j; i++) {   // 子串起始位置
        // 上述循环方式也是可以的，但在 “最长回文子序列” 一题中会有问题
        // 下面的循环方式在两个问题中都正确，这个遍历思路比较像“中心扩散法”
        for (int j = 1; j < n; j++)             // 子串结束位置
            for (int i = j - 1; i >= 0; i--) {  // 子串开始位置
                if (j == i + 1)  // 初始状态2：子串长度为 2 时，只有当两个字母相同时才是回文子串
                    dp[i][j] = (s[i] == s[j]);
                else  // 状态转移方程：当上一个状态是回文串，且此时两个位置的字母也相同时，当前状态才是回文串
                    dp[i][j] = (dp[i + 1][j - 1] && s[i] == s[j]);

                // 保存最长回文子串
                if (dp[i][j] && max_len < (j - i + 1)) {
                    max_len = j - i + 1;
                    start = i;
                }
            }

        return s.substr(start, max_len);
    }
};
```

</details>


<details><summary><b>思路2：中心扩散法（Python, TODO）</b></summary>

```python

```

</details>

---
### 有效三角形的个数 (LeetCode, No.0611, 中等, 2021-10)


[![双指针(首尾)](https://img.shields.io/badge/双指针(首尾)-lightgray.svg)](技巧-双指针(滑动窗口).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 双指针(首尾) -->

<summary><b>问题简述</b></summary> 

```text
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
```

<summary><b>思路</b></summary>

- 排序 + 首尾双指针；
- 相当于计算两数之和大于目标值的个数；


<details><summary><b>题目描述</b></summary> 

```text
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:
    输入: [2,2,3,4]
    输出: 3
    解释:
    有效的组合是: 
    2,3,4 (使用第一个 2)
    2,3,4 (使用第二个 2)
    2,2,3
注意:
    数组长度不超过1000。
    数组里整数的范围为 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```

</details>


<details><summary><b>Python</b></summary> 

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """"""
        nums = sorted(nums)
        
        cnt = 0
        for i in range(2, len(nums)):  # 注意：循环区间
            
            lo, hi = 0, i - 1
            while lo < hi:
                s = A[lo] + A[hi]
                
                if s > A[i]:
                    cnt += hi - lo  # 范围剪枝
                    hi -= 1
                else:
                    lo += 1
                    
        return cnt
```

</details>

---
### 盛最多水的容器 (LeetCode, No.0011, 中等, 2021-10)


[![双指针(首尾)](https://img.shields.io/badge/双指针(首尾)-lightgray.svg)](技巧-双指针(滑动窗口).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 双指针(首尾) -->

<summary><b>问题简述</b></summary>

```txt
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：不能倾斜容器。

示例 1：
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49 
    解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<div align="center"><img src="../_assets/question_11.jpeg" height="150" /></div>


<summary><b>思路</b></summary>

- 首尾双指针遍历


<details><summary><b>Python</b></summary>

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """"""
        l, r = 0, len(height) - 1
        ret = (r - l) * min(height[l], height[r])  # 初始化

        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            tmp = (r - l) * min(height[l], height[r])
            ret = max(ret, tmp)
            
        return ret
```

</details>

---
### 路径总和3 (LeetCode, No.0437, 中等, 2021-10)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-二叉树(树).md)
[![深度优先搜索](https://img.shields.io/badge/深度优先搜索-lightgray.svg)](算法-深度优先搜索.md)
[![前缀和](https://img.shields.io/badge/前缀和-lightgray.svg)](技巧-前缀和.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 二叉树、深度优先搜索、前缀和 -->

<summary><b>问题描述</b></summary>

```txt
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：（见图示）
    输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    输出：3
    解释：和等于 8 的路径有 3 条，如图所示。
示例 2：
    输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    输出：3

提示:
    二叉树的节点个数的范围是 [0,1000]
    -10^9 <= Node.val <= 10^9 
    -1000 <= targetSum <= 1000 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<div align="center"><img src="../_assets/pathsum3-1-tree.jpeg" height="300" /></div>


<details><summary><b>解法1：双重递归</b></summary>

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:  # noqa
        """"""
        if root is None:
            return 0

        # 双重递归
        ret = self.dfs_root(root, targetSum)
        # 把左右节点当做根节点都遍历一遍
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)

        return ret

    def dfs_root(self, root, targetSum):  # noqa
        """ 计算从根节点开始的路径数 """
        if root is None:
            return 0

        ans = 0
        if root.val == targetSum:  # 因为节点的值可能为 0，所以这里还不能直接返回
            ans += 1

        # 差值
        delta_sum = targetSum - root.val

        # 继续遍历左右子树
        ans += self.dfs_root(root.left, delta_sum)
        ans += self.dfs_root(root.right, delta_sum)
        return ans
```
</details>

<details><summary><b>解法2：前缀和+DFS</b></summary>

```python
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 保存前缀和
    prefix = defaultdict(int)
    targetSum: int

    def pathSum(self, root: TreeNode, targetSum: int) -> int:  # noqa
        """ 解法2：前缀和 + DFS """
        self.prefix[0] = 1
        self.targetSum = targetSum
        return self.dfs(root, 0)

    def dfs(self, root, cur):
        if root is None:
            return 0

        ret = 0
        cur += root.val
        ret += self.prefix[cur - self.targetSum]

        self.prefix[cur] += 1
        ret += self.dfs(root.left, cur)
        ret += self.dfs(root.right, cur)
        self.prefix[cur] -= 1

        return ret
```

</details>

---
### 重复的DNA序列 (LeetCode, No.0187, 中等, 2021-10)


[![哈希表](https://img.shields.io/badge/哈希表-lightgray.svg)](技巧-哈希表.md)
[![位运算](https://img.shields.io/badge/位运算-lightgray.svg)](技巧-位运算.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)

<!-- Tag: 哈希表、位运算 -->

<summary><b>问题简述</b></summary>

```txt
找出由 ATCG 构成的字符串中所有重复且长度为 10 的子串；
```

<summary><b>思路&考点</b></summary>

- 基本思路：哈希表计数；
- 如果直接使用子串本身作为哈希表的 key，那么时间复杂度和空间复杂度都是 `O(NL)`；而如果使用位运算+滑动窗口手动构造 key，可以把复杂度降为 `O(N)`；

<details><summary><b>题目描述</b></summary>

```txt
所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

示例 1：
    输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    输出：["AAAAACCCCC","CCCCCAAAAA"]
示例 2：
    输入：s = "AAAAAAAAAAAAA"
    输出：["AAAAAAAAAA"]

提示：
    0 <= s.length <= 10^5
    s[i] 为 'A'、'C'、'G' 或 'T'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>子串作为 key</b></summary>

- 时间&空间复杂度：`O(NL)`；
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """"""
        # from collections import defaultdict
        L = 10

        cnt = defaultdict(int)
        ans = []
        for i in range(len(s) - L + 1):
            subs = s[i: i+L]
            cnt[subs] += 1
            if cnt[subs] == 2:
                ans.append(subs)

        return ans
```

</details>

<details><summary><b>位运算+滑动窗口</b></summary>

- 时间&空间复杂度：`O(N)`；
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """"""
        # from collections import defaultdict
        L = 10
        B = {'A': 0, 'T': 1, 'C': 2, 'G': 3}  # 分别为 00, 01, 10, 11

        if len(s) < L + 1:  # assert，否则部分用例会无法通过
            return []

        # 先计算前 9 位的值
        x = 0
        for i in range(L - 1):
            b = B[s[i]]
            x = (x << 2) | b

        ans = []
        cnt = defaultdict(int)
        for i in range(len(s) - L + 1):
            b = B[s[i + L - 1]]
            # 注意该有的括号不要少，避免运算优先级混乱
            x = ((x << 2) | b) & ((1 << (L * 2)) - 1)  # 滑动计算子串的 hash 值
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i: i + L])

        return ans
```

</details>


<details><summary><b>位运算说明</b></summary>

- `(x << 2) | b`：
    ```python
    # 以为均为二进制表示
    设 x = 0010 1011, b = 10: 
    该运算相当于把 b “拼” 到 x 末尾

    x         :   0010 1011
    x = x << 2:   1010 1100
    
    x = x | b :   1010 1100
                | 0000 0010
                -----------
                  1010 1110
    ```
- `x & ((1 << (L * 2)) - 1)`
    ```python
    # 该运算把 x 除低 10 位前的所有位置置 0
    设 L = 5，x = 1110 1010 1010: 
    
    y = 1 << (L * 2):   0100 0000 0000
    y = y - 1       :   0011 1111 1111

    x = x & y       :   1110 1010 1010
                      & 0011 1111 1111
                      ----------------
                        0010 1010 1010

    ```

</details>

---
