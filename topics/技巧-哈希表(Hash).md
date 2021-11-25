# 哈希表

[Problems Index](#problems-index)

<!-- Tag: 哈希表、Hash -->

Problems Index
---
- [`No.0001` 两数之和 (LeetCode, 简单, 2021-10)](#no0001-两数之和-leetcode-简单-2021-10)
- [`No.0187` 重复的DNA序列 (LeetCode, 中等, 2021-10)](#no0187-重复的dna序列-leetcode-中等-2021-10)

---

### `No.0001` 两数之和 (LeetCode, 简单, 2021-10)


[![哈希表](https://img.shields.io/badge/哈希表-lightgray.svg)](技巧-哈希表(Hash).md)
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
### `No.0187` 重复的DNA序列 (LeetCode, 中等, 2021-10)


[![哈希表](https://img.shields.io/badge/哈希表-lightgray.svg)](技巧-哈希表(Hash).md)
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
