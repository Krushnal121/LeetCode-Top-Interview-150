class Solution {
    public void flatten(TreeNode root) {
        if (root == null)
            return;

        TreeNode current = root;
        while (current != null) {

            if (current.left != null) {
                TreeNode last = current.left;
                while (last.right != null) {
                    last = last.right;
                }

                last.right = current.right;
                current.right = current.left;
                current.left = null;
            }
            current = current.right;
        }
    }
}