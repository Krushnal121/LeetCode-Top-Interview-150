class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length==1) return new TreeNode(nums[0]);
        else{
            return helper(nums,0,nums.length);
        }
    }
    public static TreeNode helper(int[] nums, int start, int end) {
        if (start==end)return null;
        TreeNode root;
        if (end-start==1){
            root= new TreeNode(nums[start]);}
        else{
            int res=(start+end)/2;
            root=new TreeNode(nums[res]);
            root.left=helper(nums,start,res);
            root.right=helper(nums,res+1,end);
        }
        return root;
    }
}