### 最长回文子串

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

