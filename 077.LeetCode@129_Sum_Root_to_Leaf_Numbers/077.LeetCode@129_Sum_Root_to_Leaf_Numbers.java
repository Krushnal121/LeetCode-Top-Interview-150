class Solution {
    public int sumNumbers(TreeNode root) {
        if (root == null) return 0;
        String a = "";
        return find(root, a);
    }

    private int find(TreeNode root, String a) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return Integer.parseInt(a + root.val);
        return find(root.left, a + root.val) + find(root.right, a + root.val);
    }
}