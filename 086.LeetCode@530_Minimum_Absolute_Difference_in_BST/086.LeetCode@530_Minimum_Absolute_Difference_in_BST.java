class Solution {
    int min = Integer.MAX_VALUE, prev = Integer.MAX_VALUE;
    public void help(TreeNode root) {
        if (root == null)    return;
        help(root.left);
        min = Math.min(min, Math.abs(root.val - prev));
        prev = root.val;
        help(root.right);
    }
    public int getMinimumDifference(TreeNode root) {
        help(root);
        return min;
    }
}