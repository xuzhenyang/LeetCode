/*
 * @lc app=leetcode.cn id=105 lang=java
 *
 * [105] 从前序与中序遍历序列构造二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left
 * = left; this.right = right; } }
 */
class Solution {
    /**
     * 思路 
     * 前序第一个一定是root节点 在中序遍历中找到root的下标，就能将中序遍历划分为
     * 左子树[9]，root[3]，右子树[15,20,7]，并得到左子树的长度 在前序遍历，通过左子树长度位移，也能分为
     * root[3]，左子树[9]，右子树[20,15,7] 然后递归，分别从左、右子树进行同样处理
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int lp = 0;
        int rp = preorder.length - 1;
        int li = 0;
        int ri = inorder.length - 1;
        return build(preorder, inorder, lp, rp, li, ri);
    }

    private TreeNode build(int[] preorder, int[] inorder, int lp, int rp, int li, int ri) {
        if (lp > rp || li > ri) {
            return null;
        }
        int rootVal = preorder[lp];
        TreeNode root = new TreeNode(rootVal);
        for (int i = li; i <= ri; i++) {
            //在中序遍历中找到root的下标
            if (inorder[i] == rootVal) {
                //左子树长度: i - li
                root.left = build(preorder, inorder, lp + 1, lp + (i - li), li, i - 1);
                root.right = build(preorder, inorder, lp + (i - li) + 1, rp, i + 1, ri);
            }
        }
        return root;
    }

}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
// @lc code=end
