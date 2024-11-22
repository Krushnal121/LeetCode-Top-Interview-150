class Solution {
    int c = 0, ans = 0;
    public int kthSmallest(TreeNode root, int k) {
        if(root == null) {
            return 0;
        }
        kthSmallest(root.left,k);
        c++;
        if(k == c) {
            ans = root.val;
        }
        kthSmallest(root.right,k);
        return ans;
    }
}