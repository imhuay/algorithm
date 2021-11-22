### 用两个栈实现队列

<!-- Tag: 栈、队列 -->

<summary><b>问题简述</b></summary>

```txt
用两个栈实现一个队列。
队列包含两个函数 appendTail 和 deleteHead(若队列中没有元素，deleteHead 操作返回 -1 )
```

<summary><b>思路</b></summary>

- 栈：先进后出；队列：先进先出；换言之，队列就是倒序输出的栈；
- 利用双栈可实现倒序输出：维护两个栈 A 和 B，将 A 中元素依次弹出并压入栈 B，再依次弹出 B 中元素，即实现了对栈 A 元素的倒序输出，即实现了队列的性质；

<details><summary><b>题目描述</b></summary>

```txt
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
    输入：
    ["CQueue","appendTail","deleteHead","deleteHead"]
    [[],[3],[],[]]
    输出：[null,null,3,-1]
示例 2：
    输入：
    ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
    [[],[],[5],[2],[],[]]
    输出：[null,-1,null,null,5,2]

提示：
    1 <= values <= 10000
    最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>代码（Python）</b></summary>

```python
class CQueue:
    def __init__(self):
        self.I = []  # 入栈
        self.O = []  # 出栈

    def appendTail(self, value: int) -> None:
        self.I.append(value)  # 新元素全部加到 I

    def deleteHead(self) -> int:
        if self.O:  # 如果 O 不为空
            return self.O.pop()  # 弹出栈顶元素
        
        if not self.I:  # 如果 I 为空，说明队列为空
            return -1

        while self.I:  # 如果 I 不为空，但 O 为空，此时将 I 中元素依次加入 O  
            self.O.append(self.I.pop())
        return self.O.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

</details>

