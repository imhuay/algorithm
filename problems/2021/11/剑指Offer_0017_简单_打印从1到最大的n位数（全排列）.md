<!-- Tag: DFS、经典 -->

<summary><b>问题简述</b></summary>

```txt
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数（考虑大数情况）；
比如输入 3，则打印出 1~999
```

<details><summary><b>详细描述</b></summary>

```txt
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
    输入: n = 1
    输出: [1,2,3,4,5,6,7,8,9]

说明：
    用返回一个整数列表来代替打印
    n 为正整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<summary><b>思路</b></summary>

- 考虑大数情况下，直接遍历会存在越界问题；
- 本题实际考察的是数的全排列问题，同时需要去除前置 0；

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<details><summary><b>Python：不考虑大数</b></summary>

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res
```

</details>

<details><summary><b>Python：考虑大数</b></summary>

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        
        ret = []
        dig = '0123456789'
        buf = [''] * n

        def process(buf):
            """去除前置0"""
            start = 0
            while start < n and buf[start] == '0':
                start += 1
            
            return ''.join(buf[start:])

        def dfs(k):
            """DFS全排列"""
            if k == n:
                ret.append(process(buf))
                return
            
            for i in dig:  # 每一位都有 0-9 10种取法
                buf[k] = i
                dfs(k+1)

        dfs(0)
        # LeetCode要求返回 int，ret[1:] 则是因为要求从 1 开始
        return [int(it) for it in ret[1:]]
```

</details>

