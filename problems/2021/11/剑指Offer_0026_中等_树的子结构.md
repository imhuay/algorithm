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

