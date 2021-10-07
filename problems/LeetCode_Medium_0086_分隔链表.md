### 两数相加

<!-- Tag: 双指针 -->

<summary><b>问题描述</b></summary>

- 快排链表的核心操作；

```txt
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：
    输入：head = [1,4,3,2,5,2], x = 3
    输出：[1,2,2,4,3,5]
示例 2：
    输入：head = [2,1], x = 2
    输出：[1,2]
 
提示：
    链表中节点的数目在范围 [0, 200] 内
    -100 <= Node.val <= 100
    -200 <= x <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<div align="center"><img src="../_assets/partition.jpeg" height="150" /></div>


<details><summary><b>算法简述</b></summary>

```txt
新建两个链表，分别保存小于 x 和大于等于 x 的，最后拼接；
```

</details>

<details><summary><b>Python3</b></summary>

**python**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """"""
        # l/r 会进行移动，lo/hi 为头节点
        l = lo = ListNode(0)
        r = hi = ListNode(0)
        
        while head:
            if head.val < x:  # 小于 x 的拼到 lo
                l.next = head
                l = l.next
            else:  # 大于等于 x 的拼到 hi
                r.next = head
                r = r.next
                
            head = head.next
        
        # 因为不能保证最后遍历的节点在 hi 中，所以必须加上这一步，切断循坏
        r.next = None  # 关键步骤
        l.next = hi.next
        
        return lo.next
```

</details>
