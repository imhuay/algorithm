### 有效三角形的个数

<!-- Tag: 双指针 -->

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
