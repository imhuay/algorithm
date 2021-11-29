<!-- Tag: 链表、双指针 -->

<summary><b>问题简述</b></summary>

```txt
输入一个链表，输出该链表中倒数第k个节点。
```

<details><summary><b>详细描述</b></summary>

```txt
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：
    给定一个链表: 1->2->3->4->5, 和 k = 2.
    返回链表 4->5.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 前后双指针，保持两个指针相距 k 个节点，当前指针达到链表尾时，返回后指针；

<details><summary><b>Python</b></summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 1:
            return head

        cur = head
        ret = head

        while k:
            cur = cur.next
            k -= 1
        
        while cur:
            ret = ret.next
            cur = cur.next

        # 更简洁的写法，合并两个循环
        # while cur:
        #     if k <= 0: 
        #         ret = ret.next
        #     cur = cur.next
        #     k -= 1

        return ret
```

</details>

