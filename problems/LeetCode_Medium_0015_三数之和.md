### 三数之和（3Sum）
> 15. 三数之和 - 力扣（LeetCode） | https://leetcode-cn.com/problems/3sum/

Tag: 双指针

**问题简述**
```text
给定一个数组，找出该数组中所有和为 0 的三元组。
```

<details><summary><b>问题详情</b></summary> 

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
```

</details>

<details><summary><b>算法简述</b></summary> 

1. 对数组排序；
2. 先**固定一个数**，通常固定第一个数，或者最后一个，两者类似
    - 不建议固定中间位置的数（见踩坑记录）；
3. 此时左右指针分别指向**剩余部分**的首尾位置；此时若三数之和小于目标值，则右移左指针；若大于目标值，则左移右指针；

- 为避免存入重复三元组，需要循环跳过重复元素；可以使用 set 去重，但这不是考察要点，其次也存在效率问题；
- 适当进行剪枝可以提升性能；

</details>

<details><summary><b>代码</b></summary> 

**python**：时间复杂度：`O(N^2)`，空间复杂度：`O(N)`
```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 设置目标值
        target = 0

        ret = []
        L = len(nums)
        if L < 3:
            return ret

        # 排序
        nums = sorted(nums)
        for i in range(L - 2):  # 固定第一个数，注意范围
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

<details><summary><b>备忘</b></summary> 

1. 为什么不要固定中间位置的数
    - 固定第一个或最后一个数可以**缩小**每次遍历双指针的范围；
    - 但是固定中间位置的数则不会，这会带来额外的判重操作；
        
        ```python
        # 固定第一个数
        for i in range(L - 2):
            lp, rp = i + 1, L - 1  # 左指针与 i 的位置相关
        
        # 固定中间位置的数
        for i in range(1, L - 1):
            lp, rp = 0, L - 1  # 左右指针始终不变
        ```

1. 如何利用单调性剪枝
    - 在经过排序后，每轮迭代时，三数之和的最大值 `max_s` 和最小值`min_s`是确定的；
    - 所以当 `min_s > target` 或 `max_s < target` 时，后续都不可能存在等于目标值的三元组；
    - 注意：`min_s` 已经是当前的全局最小值，而 `max_s` 却不是全局最大值，所以前者可以 `break`，后者则应该 `continue`；
    - 代码细节：

        ```python
        # min_s
        if nums[i] + nums[i + 1] + nums[i + 2] > target: break
        # max_s
        if nums[i] + nums[L - 2] + nums[L - 1] < target: continue
        ```

</details>

