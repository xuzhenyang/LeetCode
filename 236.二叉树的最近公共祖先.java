/*
 * @lc app=leetcode.cn id=236 lang=java
 *
 * [236] 二叉树的最近公共祖先
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        //递归，在左右树分别找p和q
        //递归出口，找到了直接返回
        if (root == null || root == p || root == q) {
            return root;
        }
        //往左树找
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        //往右树找
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        //左边没找到，返回右树
        if (left == null) {
            return right;
        }
        //右边没找到，返回左树
        if (right == null) {
            return left;
        }
        //左右树都找到了，返回root
        return root;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
        val = x;
    }
}
// @lc code=end

