### 最长不含重复字符的子字符串

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

<div align="center"><img src="../../../_assets/剑指Offer_0048_中等_最长不含重复字符的子字符串.png" height="300" /></div>

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

