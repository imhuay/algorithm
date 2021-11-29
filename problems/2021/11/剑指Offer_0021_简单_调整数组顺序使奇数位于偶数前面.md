<!-- Tag: 数组、双指针 -->

<summary><b>问题简述</b></summary>

```txt
给定整型数组，调整其顺序，使所有奇数在偶数之前（不要求顺序）。
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

示例：
    输入：nums = [1,2,3,4]
    输出：[1,3,2,4] 
    注：[3,1,2,4] 也是正确的答案之一。
提示：
    0 <= nums.length <= 50000
    0 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 头尾双指针，当头指针指向偶数，尾指针指向奇数时，交换；
- **注意边界判断**；

<details><summary><b>Python</b></summary>

```python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:

        l, r = 0, len(nums) - 1
        while l < r:
            # 注意需要始终保持 l < r
            while l < r and nums[l] % 2 == 1:
                l += 1
            while l < r and nums[r] % 2 == 0:
                r -= 1
            
            nums[l], nums[r] = nums[r], nums[l]
        
        return nums
```

</details>

