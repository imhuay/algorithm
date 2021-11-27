# 深度优先搜索(DFS)

[Problems Index](#problems-index)

<!-- Tag: 深度优先搜索(递归)、深度优先搜索、DFS -->

Problems Index
---
- [`No.0006` 从尾到头打印链表 (剑指Offer, 简单, 2021-11)](#no0006-从尾到头打印链表-剑指offer-简单-2021-11)
- [`No.0054` 二叉搜索树的第k大节点 (剑指Offer, 简单, 2021-11)](#no0054-二叉搜索树的第k大节点-剑指offer-简单-2021-11)
- [`No.0111` 二叉树的最小深度 (LeetCode, 简单, 2021-10)](#no0111-二叉树的最小深度-leetcode-简单-2021-10)
- [`No.0437` 路径总和3 (LeetCode, 中等, 2021-10)](#no0437-路径总和3-leetcode-中等-2021-10)

---

### `No.0006` 从尾到头打印链表 (剑指Offer, 简单, 2021-11)


[![链表](https://img.shields.io/badge/链表-lightgray.svg)](数据结构-链表.md)
[![栈](https://img.shields.io/badge/栈-lightgray.svg)](数据结构-栈(单调栈)、队列.md)
[![DFS](https://img.shields.io/badge/DFS-lightgray.svg)](算法-深度优先搜索(DFS).md)
[![递归](https://img.shields.io/badge/递归-lightgray.svg)](算法-递归、迭代.md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)
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

<!-- <div align="center"><img src="../_assets/xxx.png" height="300" /></div> -->

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

---
### `No.0054` 二叉搜索树的第k大节点 (剑指Offer, 简单, 2021-11)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树、二叉树.md)
[![dfs](https://img.shields.io/badge/dfs-lightgray.svg)](算法-深度优先搜索(DFS).md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)
<!-- Tag: 二叉树、dfs -->

<summary><b>问题简述</b></summary>

```txt
给定一棵二叉搜索树，请找出其中第k大的节点。
```

<summary><b>思路</b></summary>

- 二叉搜索树的性质：中序遍历的结果为递增序列；
- 为了得到第 K 大，需要递减序列，“反向”中序遍历即可：即按“右中左”的顺序深度搜索；
- 利用辅助变量提前结束搜索；

<details><summary><b>题目描述</b></summary>

```txt
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
    输入: root = [3,1,4,null,2], k = 1
     3
    / \
   1   4
    \
     2
    输出: 4
示例 2:
    输入: root = [5,3,6,2,4,null,null,1], k = 3
        5
       / \
      3   6
     / \
    2   4
   /
  1
    输出: 4

限制：
    1 ≤ k ≤ 二叉搜索树元素个数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>思路：反向中序遍历（C++）</b></summary>

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    int k;
    int ret;
public:
    int kthLargest(TreeNode* root, int k) {
        this->k = k;
        inOrder(root);
        return this->ret;
    }

    void inOrder(TreeNode* node) {
        if (node == nullptr) return;

        inOrder(node->right);  // 先遍历右子树
        if (this->k == 0) return;
        this->k -= 1;
        if (this->k == 0) this->ret = node->val;
        inOrder(node->left);
    }
};
```

</details>

---
### `No.0111` 二叉树的最小深度 (LeetCode, 简单, 2021-10)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树、二叉树.md)
[![DFS](https://img.shields.io/badge/DFS-lightgray.svg)](算法-深度优先搜索(DFS).md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)
<!-- Tag: 二叉树，DFS -->

<summary><b>问题简述</b></summary>

```txt
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

示例：
    给定二叉树 [3,9,20,null,null,15,7]，
        3
       / \
      9  20
        /  \
       15   7
    返回它的最小深度 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<summary><b>思路</b></summary>

- 深度优先搜索，记录过程中的最小深度；

<details><summary><b>深度优先搜索（Python）</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """"""
        if not root:  # 尾递归1
            return 0

        if not root.left and not root.right:  # 尾递归 2 *
            return 1
        
        min_depth = 10**5 + 10
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        
        return min_depth + 1
```

</details>

---
### `No.0437` 路径总和3 (LeetCode, 中等, 2021-10)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树、二叉树.md)
[![深度优先搜索](https://img.shields.io/badge/深度优先搜索-lightgray.svg)](算法-深度优先搜索(DFS).md)
[![前缀和](https://img.shields.io/badge/前缀和-lightgray.svg)](技巧-前缀和.md)
[![LeetCode](https://img.shields.io/badge/LeetCode-lightgray.svg)](题集-LeetCode.md)
<!-- Tag: 二叉树、深度优先搜索、前缀和 -->

<summary><b>问题描述</b></summary>

```txt
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：（见图示）
    输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    输出：3
    解释：和等于 8 的路径有 3 条，如图所示。
示例 2：
    输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    输出：3

提示:
    二叉树的节点个数的范围是 [0,1000]
    -10^9 <= Node.val <= 10^9 
    -1000 <= targetSum <= 1000 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<div align="center"><img src="../_assets/pathsum3-1-tree.jpeg" height="300" /></div>


<details><summary><b>解法1：双重递归</b></summary>

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:  # noqa
        """"""
        if root is None:
            return 0

        # 双重递归
        ret = self.dfs_root(root, targetSum)
        # 把左右节点当做根节点都遍历一遍
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)

        return ret

    def dfs_root(self, root, targetSum):  # noqa
        """ 计算从根节点开始的路径数 """
        if root is None:
            return 0

        ans = 0
        if root.val == targetSum:  # 因为节点的值可能为 0，所以这里还不能直接返回
            ans += 1

        # 差值
        delta_sum = targetSum - root.val

        # 继续遍历左右子树
        ans += self.dfs_root(root.left, delta_sum)
        ans += self.dfs_root(root.right, delta_sum)
        return ans
```
</details>

<details><summary><b>解法2：前缀和+DFS</b></summary>

```python
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 保存前缀和
    prefix = defaultdict(int)
    targetSum: int

    def pathSum(self, root: TreeNode, targetSum: int) -> int:  # noqa
        """ 解法2：前缀和 + DFS """
        self.prefix[0] = 1
        self.targetSum = targetSum
        return self.dfs(root, 0)

    def dfs(self, root, cur):
        if root is None:
            return 0

        ret = 0
        cur += root.val
        ret += self.prefix[cur - self.targetSum]

        self.prefix[cur] += 1
        ret += self.dfs(root.left, cur)
        ret += self.dfs(root.right, cur)
        self.prefix[cur] -= 1

        return ret
```

</details>

---
