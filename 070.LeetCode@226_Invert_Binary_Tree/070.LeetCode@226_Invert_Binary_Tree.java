class Solution {
    public static TreeNode invertTree(TreeNode root) {
        if (root == null || root.left==root.right) return root;
        TreeNode tempright=invertTree(root.left);
        TreeNode templeft=invertTree(root.right);
        root.right=tempright;
        root.left=templeft;
        return root;
    }
}