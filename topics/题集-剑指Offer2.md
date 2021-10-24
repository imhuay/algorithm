# 剑指Offer2

[Problems Index](#problems-index)

<!-- Tag: 剑指Offer2 -->

Problems Index
---
- [山峰数组的顶部 (剑指Offer2, No.0069, 简单, 2021-10)](#山峰数组的顶部-剑指offer2-no0069-简单-2021-10)
- [数组中的第K大的数字 (剑指Offer2, No.0076, 中等, 2021-10)](#数组中的第k大的数字-剑指offer2-no0076-中等-2021-10)

---

### 山峰数组的顶部 (剑指Offer2, No.0069, 简单, 2021-10)


[![二分查找](https://img.shields.io/badge/二分查找-lightgray.svg)](算法-二分查找.md)
[![剑指Offer2](https://img.shields.io/badge/剑指Offer2-lightgray.svg)](题集-剑指Offer2.md)

<!-- Tag: 二分查找、剑指Offer2 -->

<summary><b>问题简述</b></summary>

```txt
找出山脉数组中山峰的下标（保证给出的数组是一个山脉数组）
```

<summary><b>思路</b></summary>

- 当 `N[mid] > N[mid+1]` 时，山峰必在左侧；反之，在右侧；
- 因为从中间划分后，左右分别满足相反的性质，因此可以使用二分查找；

<details><summary><b>题目描述</b></summary>

```txt
符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：

    arr.length >= 3
    存在 i（0 < i < arr.length - 1）使得：
        arr[0] < arr[1] < ... arr[i-1] < arr[i]
        arr[i] > arr[i+1] > ... > arr[arr.length - 1]
    
    给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。

示例 1：
    输入：arr = [0,1,0]
    输出：1
示例 2：
    输入：arr = [1,3,5,4,2]
    输出：2
示例 3：
    输入：arr = [0,10,5,2]
    输出：1
示例 4：
    输入：arr = [3,4,5,1]
    输出：2
示例 5：
    输入：arr = [24,69,100,99,79,78,67,36,26,19]
    输出：2

提示：
    3 <= arr.length <= 10^4
    0 <= arr[i] <= 10^6
    题目数据保证 arr 是一个山脉数组
 
进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/B1IidL
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>Python</b></summary>

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """"""
        left, right = 1, len(arr) - 2

        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid + 1]:  # 山峰在左侧
                ans = mid  # 目前已知 mid 位置的值是最大的，因为保证 arr 是一个山脉数组，所以一定会来到这个分支
                right = mid - 1
            else:  # 山峰在右侧
                left = mid + 1

        return ans
```

</details>

---
### 数组中的第K大的数字 (剑指Offer2, No.0076, 中等, 2021-10)


[![堆](https://img.shields.io/badge/堆-lightgray.svg)](数据结构-优先队列(堆).md)
[![分治](https://img.shields.io/badge/分治-lightgray.svg)](算法-分治.md)
[![快排](https://img.shields.io/badge/快排-lightgray.svg)](算法-排序.md)
[![剑指Offer2](https://img.shields.io/badge/剑指Offer2-lightgray.svg)](题集-剑指Offer2.md)

<!-- Tag: 堆、分治、快排、剑指Offer2 -->

<summary><b>问题简述</b></summary>

```txt
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
```

<details><summary><b>题目描述</b></summary>

```txt
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
示例 2:
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4

提示：
    1 <= k <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xx4gT2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>思路1：partition操作（分治）</b></summary>

- partition操作描述：先随机确定一个锚点，然后将数组划分为小于锚点和大于锚点的两部分呢；

```python
import random


class Solution:
    """"""

    def findKthLargest(self, nums: List[int], k: int) -> int:  # noqa
        """"""
        lo, hi = 0, len(nums) - 1

        while True:  # 第 k 大，排序后期下标应该是 k - 1
            idx = self.partition(nums, lo, hi)
            if idx + 1 == k:
                return nums[idx]
            elif idx + 1 < k:
                lo = idx + 1
            else:
                hi = idx - 1

    def partition(self, nums: List[int], lo: int, hi: int) -> int:
        """"""
        # === 挑选锚点 ===
        # 方式1）默认选 lo 作为锚点
        # pivot = nums[lo]

        # 方式2）随机选择一个锚点，并把锚点固定到首位或末位，这里交换到首位
        flag = random.randint(lo, hi)
        pivot = nums[flag]
        nums[flag], nums[lo] = nums[lo], nums[flag]

        # === partition 操作 ===
        # 方式1）单向遍历
        idx = lo  # 记录锚点在数组中的升序顺位
        for i in range(lo + 1, hi + 1):
            if nums[i] > pivot:  # 找到一个大于锚点的值
                idx += 1
                nums[idx], nums[i] = nums[i], nums[idx]

        nums[idx], nums[lo] = nums[lo], nums[idx]  # 把锚点交换到 idx 的位置

        return idx

        # 方式2）左右交换
        # l, r = lo, hi
        # while l < r:
        #     while l < r and nums[r] <= pivot:
        #         r -= 1
        #     while l < r and nums[l] >= pivot:
        #         l += 1
        #     if l < r:
        #         nums[l], nums[r] = nums[r], nums[l]
        # nums[lo], nums[l] = nums[l], nums[lo]
        #
        # return l
```

</details>


<details><summary><b>思路2：大顶堆（Python，调库）</b></summary>

```python
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """"""
        heap = []
        
        for x in nums:
            heapq.heappush(heap, -x)  # 默认是小顶堆，这里传入 -x，模拟大顶堆
            
        for _ in range(k - 1):
            heapq.heappop(heap)
            
        return -heap[0]
```

</details>

---
