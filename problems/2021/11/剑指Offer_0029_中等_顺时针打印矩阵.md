<!-- Tag: 数组、模拟、经典 -->

<summary><b>问题简述</b></summary>

```txt
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]
示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1：模拟</b></summary>

- 循环遍历 4 个方向的路线，中间做好边界判断（虽然思路简单，但是写起来很容易出错）；

<details><summary><b>Python</b></summary>

```python
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        """"""        
        ret = []
        if not matrix:
            return ret

        m, n = len(matrix), len(matrix[0])  # m行n列
        # 设置左、右、上、下边界
        l, r, t, b, = 0, n - 1, 0, m - 1

        while True:
            # 依次遍历 4 个方向
            # 因为最后一趟遍历哪个方向都有可能，所以需要 4 个 break

            # left to right, top+=1
            for i in range(l, r + 1):
                ret.append(matrix[t][i])
            t += 1
            if t > b:
                break

            # top to bottom, right-=1
            for i in range(t, b + 1):
                ret.append(matrix[i][r])
            r -= 1
            if l > r:
                break

            # right to left, bottom-=1
            for i in range(r, l - 1, -1):  # 逆序
                ret.append(matrix[b][i])
            b -= 1
            if t > b:
                break

            # bottom to top, left+=1
            for i in range(b, t - 1, -1):  # 逆序
                ret.append(matrix[i][l])
            l += 1
            if l > r:
                break

        return ret
```

</details>


<summary><b>思路2：只遍历一个方向</b></summary>

- 每次从左往右遍历完第一层后，把原来的矩阵逆时针旋转 90 度；
- 这样下一次遍历依然只要从左往右走就可以了；
- 而**逆时针旋转的操作在 python 中可以用一行代码完成！**

<details><summary><b>Python</b></summary>

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            ret += list(matrix.pop(0))  # zip 后的结果是一个元组，这里转成 list，不过实际上不转换也可以；

            # 核心操作，逆时针旋转 90 度
            matrix = list(zip(*matrix))[::-1]
        
        return ret
```

```python
# 图解 `list(zip(*matrix))[::-1]` 这一步做了什么：

# 假设已经 pop 了第一行，此时矩阵剩余的部分是：
[4 5 6]  # 记为 l1
[7 8 9]  # 记为 l2，如果有 n 行，则记为 ln

# zip(*matrix) 包含了两个知识点：一个是 zip() 函数，一个是 * 号的作用；
# zip(*matrix) 实际上等价于 zip(l1, l2, ..., ln)
# 经过这一步 matrix 将转化为（相当于做了一次转置）
[4 7]
[5 8]
[6 9]

# 这时再将 matrix 做一次逆序，就得到了逆时针旋转 90 度的结果
[6 9]
[5 8]
[4 7]

```

</details>
