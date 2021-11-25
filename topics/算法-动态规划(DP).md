# 动态规划(DP)

[Problems Index](#problems-index)

<!-- Tag: 动态规划、DP -->


## 理解

- 动态规划是**记忆化搜索**的一种特殊形式；
- 一般思路：当子问题的结果需要被重复利用（存在大量重复计算） -> 记忆化搜索 -> 动态规划（迭代）；

## 步骤

**状态定义**

**转移方程**

**初始状态**

## 难点

- 动态规划关键是找到**初始状态**和**状态转移方程**；
    - 有些问题的状态并不是问题本身，需要重新构造，也是一个难点；

Problems Index
---
- [`No.0005` 最长回文子串 (LeetCode, 中等, 2021-10)](#no0005-最长回文子串-leetcode-中等-2021-10)
- [`No.0042` 连续子数组的最大和 (剑指Offer, 简单, 2021-10)](#no0042-连续子数组的最大和-剑指offer-简单-2021-10)
- [`No.0047` 礼物的最大价值 (剑指Offer, 中等, 2021-11)](#no0047-礼物的最大价值-剑指offer-中等-2021-11)
- [`No.0048` 最长不含重复字符的子字符串 (剑指Offer, 中等, 2021-11)](#no0048-最长不含重复字符的子字符串-剑指offer-中等-2021-11)

---

### `No.0005` 最长回文子串 (LeetCode, 中等, 2021-10)


[![DP](https://img.shields.io/badge/DP-lightgray.svg)](算法-动态规划(DP).md)
[![模拟](https://img.shields.io/badge/模拟-lightgray.svg)](基础-模拟、数学、找规律.md)
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
### `No.0042` 连续子数组的最大和 (剑指Offer, 简单, 2021-10)


[![前缀和](https://img.shields.io/badge/前缀和-lightgray.svg)](技巧-前缀和.md)
[![动态规划](https://img.shields.io/badge/动态规划-lightgray.svg)](算法-动态规划(DP).md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 前缀和、动态规划 -->

<summary><b>问题简述</b></summary>

```txt
给定一个整型数组，求其连续子数组的最大和。
```

<details><summary><b>题目描述</b></summary>

```txt
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。
 

示例1:
    输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

提示：
    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>代码：动态规划（Python）</b></summary>

- **状态定义**：记 `dp[i]` 表示以元素 `nums[i]` 结尾的连续子数组最大和；
- **转移方程**：
    - 当 $dp[i-1] > 0$ 时：执行 $dp[i] = dp[i-1] + nums[i]$；
    - 当 $dp[i-1] \le 0$ 时：执行 $dp[i] = nums[i]$；

- 时间复杂度：`O(N)`；
- 空间复杂度：`O(1)`，实际上不需要存储所有状态，只需要保存 `dp[i-1]` 即可（滚动数组）；

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """"""
        dp = 0
        ret = nums[0]
        for i in range(len(nums)):
            if dp > 0:
                dp = dp + nums[i]
            else:
                dp = nums[i]

            ret = max(ret, dp)
        
        return ret
```

</details>


<details><summary><b>代码：前缀和（Python）</b></summary>

- 最大连续子数组 = 最大前缀和 - 最小前缀和

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """"""
        ret = nums[0]
        pre_sum = 0
        min_pre_sum = 0

        for i in range(len(nums)):
            pre_sum += nums[i]
            ret = max(ret, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        
        return ret
```

</details>

---
### `No.0047` 礼物的最大价值 (剑指Offer, 中等, 2021-11)


[![动态规划](https://img.shields.io/badge/动态规划-lightgray.svg)](算法-动态规划(DP).md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 动态规划 -->

<summary><b>问题简述</b></summary>

```txt
给定 m*n 的整型数组 grid，求从左上角到右下角路线中和的最大值（每次向下或向右移动一格）

示例 1:
    输入: 
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 12
    解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
```

<summary><b>思路：动态规划（无优化）</b></summary>

**状态定义**
- 记 `dp[i][j] := 从左上角走至 (i,j) 位置时的最大值` 

**转移方程**
- `dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]`

**初始状态**
- `dp[0][0] = grid[0][0]`
- `dp[i][0] = sum(grid[:i][0])`
- `dp[0][j] = sum(grid[0][:j])`

<details><summary><b>题目描述</b></summary>

```txt
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:
    输入: 
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 12
    解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 
提示：
    0 < grid.length <= 200
    0 < grid[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>动态规划（Python）</b></summary>

因为 `dp[i][j]` 只与 `dp[i-1][j]` 和 `dp[i][j-1]` 有关，因此可以直接将 grid 作为 dp 矩阵，原地修改；
> [题解：礼物的最大价值（动态规划，清晰图解）](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/)

```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 初始化
        for j in range(1, n): 
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]
```

</details>

---
### `No.0048` 最长不含重复字符的子字符串 (剑指Offer, 中等, 2021-11)


[![动态规划](https://img.shields.io/badge/动态规划-lightgray.svg)](算法-动态规划(DP).md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 动态规划 -->

<summary><b>问题简述</b></summary>

```txt
求字符串 s 中最长的不包含重复字符的子串，返回其长度；
```

<summary><b>思路：动态规划</b></summary>

**状态定义**
- 记 `dp[j] := 以第 j 个字符为结尾的不含重复字符的子串的最大长度`；

**转移方程**
```
dp[j] = dp[j-1] + 1     if dp[j-1] <  j-i
      = j-i             if dp[j-1] >= j-i

其中 i 表示字符 s[j] 上一次出现的位置；
```

- 使用一个 hash 表记录每个字符上一次出现的位置；
- 因为当前状态只与上一个状态有关，因此可以使用一个变量代替数组（滚动）；

**初始状态**
- `dp[0] = 1`

**图解**
> [最长不含重复字符的子字符串（动态规划 / 双指针 + 哈希表，清晰图解）](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/mian-shi-ti-48-zui-chang-bu-han-zhong-fu-zi-fu-d-9/)

<div align="center"><img src="../_assets/剑指Offer_0048_中等_最长不含重复字符的子字符串.png" height="300" /></div>

<details><summary><b>题目描述</b></summary>

```txt
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
    输入: "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
    s.length <= 40000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>代码：动态规划+哈希表（Python）</b></summary>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx = dict()  # 记录每个字符上一次出现的位置
        ret = dp = 0
        for j in range(len(s)):
            if s[j] not in idx:
                dp = dp + 1
            else:
                i = idx[s[j]]  # 获取位置 i
                if dp < j - i:
                    dp = dp + 1
                else:
                    dp = j - i

            idx[s[j]] = j  # 更新位置 i
            ret = max(ret, dp)  # 更新最大长度
        return ret
```

</details>

---
