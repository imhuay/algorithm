# 广度优先搜索(BFS)

[Problems Index](#problems-index)

<!-- Tag: 广度优先搜索、BFS -->

Problems Index
---
- [`剑指Offer No.0032 层序遍历二叉树-1 (简单, 2021-11)`](#剑指offer-no0032-层序遍历二叉树-1-简单-2021-11)
- [`剑指Offer No.0032 层序遍历二叉树-2 (简单, 2021-11)`](#剑指offer-no0032-层序遍历二叉树-2-简单-2021-11)
- [`剑指Offer No.0032 层序遍历二叉树-3（之字形遍历） (简单, 2021-11)`](#剑指offer-no0032-层序遍历二叉树-3之字形遍历-简单-2021-11)

---

### `剑指Offer No.0032 层序遍历二叉树-1 (简单, 2021-11)`


[![BFS](https://img.shields.io/badge/BFS-lightgray.svg)](算法-广度优先搜索(BFS).md)
[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树、二叉树.md)
[![队列](https://img.shields.io/badge/队列-lightgray.svg)](数据结构-栈(单调栈)、队列.md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)
<!-- Tag: BFS、二叉树、队列 -->

<summary><b>问题简述</b></summary>

```txt
层序遍历二叉树
```

<details><summary><b>详细描述</b></summary>

```txt
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
    给定二叉树: [3,9,20,null,null,15,7],

        3
    / \
    9  20
        /  \
    15   7
返回：
    [3,9,20,15,7]
 
提示：
    节点总数 <= 1000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<summary><b>思路</b></summary>

- 利用辅助队列 q；
    1. 将树的根结点入队；
    2. 如果 q 不为空，则将头结点出队记为 node；如果 node 的左节点不为空，则将左节点入队；如果 node 的右节点不为空，则将右节点入队；
    3. 重复 2、3，直到 q 为空


<details><summary><b>Python</b></summary>

- `list` 也可以模拟队列，为什么还要用 `collections.deque`？
    - `list.pop(0)` 的时间复杂度为 `O(N)`；而 `deque.popleft()` 只要 `O(1)`；

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        from collections import deque

        if not root: return []

        buf = deque([root])  # 队列
        ret = []
        while buf:
            cur = buf.popleft()  # 弹出队列头
            ret.append(cur.val)

            if cur.left:
                buf.append(cur.left)
            if cur.right:
                buf.append(cur.right)
        
        return ret
```

</details>


<details><summary><b>C++</b></summary>

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

public:
    vector<int> levelOrder(TreeNode* root) {
        
        vector<int> ret;
        queue<TreeNode*> q;  // 辅助队列
        
        if (root)
            q.push(root);

        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();

            ret.push_back(node->val);
            if (node->left) {
                q.push(node->left);
            }
            if (node->right) {
                q.push(node->right);
            }
        }

        return ret;
    }
};
```

</details>

---
### `剑指Offer No.0032 层序遍历二叉树-2 (简单, 2021-11)`


[![BFS](https://img.shields.io/badge/BFS-lightgray.svg)](算法-广度优先搜索(BFS).md)
[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树、二叉树.md)
[![队列](https://img.shields.io/badge/队列-lightgray.svg)](数据结构-栈(单调栈)、队列.md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)
<!-- Tag: BFS、二叉树、队列 -->

<summary><b>问题简述</b></summary>

```txt
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
```

<details><summary><b>详细描述</b></summary>

```txt
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
    给定二叉树: [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    返回其层次遍历结果：
    [
        [3],
        [9,20],
        [15,7]
    ]

提示：
    节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 相比 “层序遍历二叉树-1”，本题需要同时记录当前层的节点数量（写法1）；
- 实际上每一层的节点数量包含在了保存的队列信息中，详见（写法2）；

<details><summary><b>Python：写法1</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if not root: return []

        buf = deque([root])
        cnt = 1  # 记录当前层的节点数量
        ret = []
        while buf:
            tmp = []  # 记录层结果
            for _ in range(cnt):  # 循环当前层节点数量的次数，期间改变 cnt 不会影响遍历次数
                cur = buf.popleft()
                tmp.append(cur.val)
                cnt -= 1

                if cur.left:
                    buf.append(cur.left)
                    cnt += 1
                if cur.right:
                    buf.append(cur.right)
                    cnt += 1
            ret.append(tmp)

        return ret
```

</details>

<details><summary><b>Python：写法2</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if not root: return []

        buf = deque([root])
        ret = []
        while buf:
            tmp = []
            for _ in range(len(buf)):
                cur = buf.popleft()
                tmp.append(cur.val)
                
                if cur.left:
                    buf.append(cur.left)
                if cur.right:
                    buf.append(cur.right)
            
            ret.append(tmp)
        
        return ret
```

</details>

---
### `剑指Offer No.0032 层序遍历二叉树-3（之字形遍历） (简单, 2021-11)`


[![BFS](https://img.shields.io/badge/BFS-lightgray.svg)](算法-广度优先搜索(BFS).md)
[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树、二叉树.md)
[![队列](https://img.shields.io/badge/队列-lightgray.svg)](数据结构-栈(单调栈)、队列.md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)
<!-- Tag: BFS、二叉树、队列 -->

<summary><b>问题简述</b></summary>

```txt
按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
```

<details><summary><b>详细描述</b></summary>

```txt
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
    给定二叉树: [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回其层次遍历结果：

    [
        [3],
        [20,9],
        [15,7]
    ]

提示：
    节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路</b></summary>

- 在“层序遍历二叉树-2”的基础上，加入奇偶层的处理即可；

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if not root: return []

        buf = deque([root])
        lv = 1  # 记录当前层数
        cnt = 1  # 记录当前层的节点数
        ret = []
        while buf:
            tmp = []
            for _ in range(cnt):
                cur = buf.popleft()
                tmp.append(cur.val)
                cnt -= 1

                if cur.left:
                    buf.append(cur.left)
                    cnt += 1
                if cur.right:
                    buf.append(cur.right)
                    cnt += 1
            
            # 上面的代码跟 层序遍历二叉树-2 完全相同，
            # 在将 tmp 加入 ret 时，对偶数层的 tmp 做一下倒序
            if lv & 1:  # 奇数层
                ret.append(tmp)
            else:
                ret.append(tmp[::-1])
            lv += 1
        
        return ret
```

</details>

---
