# 剑指Offer

[Problems Index](#problems-index)

<!-- Tag: 剑指Offer -->

Problems Index
---
- [`No.0026` 树的子结构 (剑指Offer, 中等, 2021-11)](#no0026-树的子结构-剑指offer-中等-2021-11)
- [`No.0027` 二叉树的镜像 (剑指Offer, 简单, 2021-11)](#no0027-二叉树的镜像-剑指offer-简单-2021-11)
- [`No.0028` 对称的二叉树 (剑指Offer, 简单, 2021-11)](#no0028-对称的二叉树-剑指offer-简单-2021-11)
- [`No.0032` 层序遍历二叉树 (剑指Offer, 中等, 2021-11)](#no0032-层序遍历二叉树-剑指offer-中等-2021-11)
- [`No.0042` 连续子数组的最大和 (剑指Offer, 简单, 2021-10)](#no0042-连续子数组的最大和-剑指offer-简单-2021-10)
- [`No.0054` 二叉搜索树的第k大节点 (剑指Offer, 简单, 2021-11)](#no0054-二叉搜索树的第k大节点-剑指offer-简单-2021-11)
- [`No.0055` 二叉树的深度 (剑指Offer, 简单, 2021-11)](#no0055-二叉树的深度-剑指offer-简单-2021-11)

---

### `No.0026` 树的子结构 (剑指Offer, 中等, 2021-11)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树(二叉树).md)
[![递归](https://img.shields.io/badge/递归-lightgray.svg)](算法-递归(迭代).md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 二叉树、递归 -->

<summary><b>问题简述</b></summary>

```txt
输入两棵二叉树A和B，判断B是不是A的子结构(约定空树不是任意一个树的子结构)
```

<summary><b>思路</b></summary>

> [树的子结构（先序遍历 + 包含判断，清晰图解）](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/mian-shi-ti-26-shu-de-zi-jie-gou-xian-xu-bian-li-p/)

1. 先序遍历 A，然后确定 B 是否为 A 的子结构；
2. 如何确定子结构：
    - 如果 B 的根节点与 A 的某子节点 C 相等；
    - 递归判断 C 和 B 的左子节点是否相等；
    - 递归判断 C 和 B 的右子节点是否相等；
3. 确定尾递归；

<details><summary><b>题目描述</b></summary>

```txt
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
    给定的树 A:
         3
        / \
       4   5
      / \
     1   2
    
    给定的树 B：
       4 
      /
     1
    返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
    输入：A = [1,2,3], B = [3,1]
    输出：false
示例 2：
    输入：A = [3,4,5,1,2], B = [4,1]
    输出：true

限制：
    0 <= 节点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>递归（C++）</b></summary>

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
    bool isSubStructure(TreeNode* A, TreeNode* B) {
        if (A == nullptr || B == nullptr) return false;

        return isSubTree(A, B)
            || isSubStructure(A->left, B) 
            || isSubStructure(A->right, B);
    }

    bool isSubTree(TreeNode* A, TreeNode* B) {
        if (B == nullptr) return true; 
        if (A == nullptr) return false;

        if (A->val == B->val) {
            return isSubTree(A->left, B->left) && isSubTree(A->right, B->right);
        } else {
            return false;
        }
    }
};
```

</details>

---
### `No.0027` 二叉树的镜像 (剑指Offer, 简单, 2021-11)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树(二叉树).md)
[![递归](https://img.shields.io/badge/递归-lightgray.svg)](算法-递归(迭代).md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 二叉树、递归 -->

<summary><b>问题简述</b></summary>

```txt
输入一个二叉树，输出它的镜像。
```

<summary><b>思路</b></summary>

- 所谓镜像，实际上就是调换左右子树，然后递归应用到所有子树；
- 参考 `def swap(a,b): a, b = b, a`

<details><summary><b>题目描述</b></summary>

```txt
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：
    输入：root = [4,2,7,1,3,6,9]
    输出：[4,7,2,9,6,3,1]

限制：
    0 <= 节点个数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>递归（python）</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """"""
        if root is None: return None

        # 交换左右子树
        root.left, root.right = root.right, root.left

        # 递归应用到左右子树
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        return root
```

</details>

---
### `No.0028` 对称的二叉树 (剑指Offer, 简单, 2021-11)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树(二叉树).md)
[![递归](https://img.shields.io/badge/递归-lightgray.svg)](算法-递归(迭代).md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 二叉树、递归 -->

<summary><b>问题简述</b></summary>

```txt
判断一棵二叉树是不是对称的。
```

<summary><b>思路</b></summary>

- 注意除了根节点外，比较的左右子树并不是来自同一个节点；

<div align="center"><img src="../_assets/图解对称的二叉树.png" height="200" /></div>

<details><summary><b>题目描述</b></summary>

```txt
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

示例 1：
    输入：root = [1,2,2,3,4,4,3]
    输出：true
示例 2：
    输入：root = [1,2,2,null,3,null,3]
    输出：false
 

限制：
    0 <= 节点个数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>递归（C++）</b></summary>

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
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) 
            return true;

        return dfs(root->left, root->right);
    }

    bool dfs(TreeNode* l, TreeNode* r) {  // 注意，出了根节点外，l 和 r 并不是同一节点的左右子树，理解这一点很重要
        if (l == nullptr && r == nullptr) 
            return true;
        if (l == nullptr || r == nullptr) 
            return false;
            
        if (l->val == r->val) {
            return dfs(l->left, r->right) && dfs(l->right, r->left);
        } else {
            return false;
        }

    }
};
```

</details>

---
### `No.0032` 层序遍历二叉树 (剑指Offer, 中等, 2021-11)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树(二叉树).md)
[![队列](https://img.shields.io/badge/队列-lightgray.svg)](数据结构-队列.md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 二叉树、队列 -->

<summary><b>问题简述</b></summary>

```txt
层序遍历二叉树
```

<summary><b>思路</b></summary>

- 利用辅助队列 q；
    1. 将树的根结点入队；
    2. 如果 q 不为空，则将头结点出队记为 node；如果 node 的左节点不为空，则将左节点入队；如果 node 的右节点不为空，则将右节点入队；
    3. 重复 2、3，直到 q 为空

<details><summary><b>题目描述</b></summary>

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


<details><summary><b>思路：队列（C++）</b></summary>

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
### `No.0042` 连续子数组的最大和 (剑指Offer, 简单, 2021-10)


[![前缀和](https://img.shields.io/badge/前缀和-lightgray.svg)](技巧-前缀和.md)
[![DP](https://img.shields.io/badge/DP-lightgray.svg)](算法-动态规划.md)
[![分治](https://img.shields.io/badge/分治-lightgray.svg)](算法-分治.md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 前缀和、DP、分治 -->

<summary><b>问题简述</b></summary>

```txt
给定一个整型数组，求其连续子数组的最大和。
```

<details><summary><b>题目描述</b></summary>

```txt
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。
 

示例1:
    输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

提示：
    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>


<details><summary><b>动态规划（Python）</b></summary>

- **状态定义**：记 `dp[i]` 表示以元素 `nums[i]` 结尾的连续子数组最大和；
- **转移方程**：
    - 当 $dp[i-1] > 0$ 时：执行 $dp[i] = dp[i-1] + nums[i]$；
    - 当 $dp[i-1] \le 0$ 时：执行 $dp[i] = nums[i]$；

- 时间复杂度：`O(N)`；
- 空间复杂度：`O(1)`，实际上不需要存储所有状态，只需要保存 `dp[i-1]` 即可（滚动数组）；

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """"""
        dp = 0
        ret = nums[0]
        for i in range(len(nums)):
            if dp > 0:
                dp = dp + nums[i]
            else:
                dp = nums[i]

            ret = max(ret, dp)
        
        return ret
```

</details>


<details><summary><b>前缀和（Python）</b></summary>

- 最大连续子数组 = 最大前缀和 - 最小前缀和

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """"""
        ret = nums[0]
        pre_sum = 0
        min_pre_sum = 0

        for i in range(len(nums)):
            pre_sum += nums[i]
            ret = max(ret, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        
        return ret
```

</details>


<details><summary><b>分治（Python）</b></summary>

TODO

</details>

---
### `No.0054` 二叉搜索树的第k大节点 (剑指Offer, 简单, 2021-11)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树(二叉树).md)
[![dfs](https://img.shields.io/badge/dfs-lightgray.svg)](算法-深度优先搜索.md)
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
### `No.0055` 二叉树的深度 (剑指Offer, 简单, 2021-11)


[![二叉树](https://img.shields.io/badge/二叉树-lightgray.svg)](数据结构-树(二叉树).md)
[![递归](https://img.shields.io/badge/递归-lightgray.svg)](算法-递归(迭代).md)
[![剑指Offer](https://img.shields.io/badge/剑指Offer-lightgray.svg)](题集-剑指Offer.md)

<!-- Tag: 二叉树、递归 -->

<summary><b>问题简述</b></summary>

```txt
输入一棵二叉树的根节点，求该树的深度。
```

<summary><b>思路</b></summary>

- 递归公式：`最大深度 := 1 + 子树的最大深度`

<details><summary><b>题目描述</b></summary>

```txt
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

提示：
    节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

<!-- <div align="center"><img src="./_assets/xxx.png" height="300" /></div> -->

</details>


<details><summary><b>递归（C++）</b></summary>

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
    int maxDepth(TreeNode* root) {
        if (root == NULL) return 0;

        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```

</details>

---
