<!-- Tag: 链表、栈、DFS、递归 -->

<summary><b>问题简述</b></summary>

```txt
从尾到头打印链表（用数组返回）
```

<summary><b>思路</b></summary>

**思路1**：
- 利用栈，顺序入栈，然后依次出栈即可

**思路2**：
- 利用深度优先遍历思想（二叉树的先序遍历）

<details><summary><b>题目描述</b></summary>

```txt
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
    输入：head = [1,3,2]
    输出：[2,3,1]

限制：
    0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>代码：栈（Python）</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        # ret = []
        # for _ in range(len(stack)):  # 相当于逆序遍历
        #     ret.append(stack.pop())
        # return ret
        return stack[::-1]  # 与以上代码等价
```

</details>

<details><summary><b>代码：DFS、递归（Python）</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []

        ret = self.reversePrint(head.next)
        ret.append(head.val)

        return ret
```

</details>

