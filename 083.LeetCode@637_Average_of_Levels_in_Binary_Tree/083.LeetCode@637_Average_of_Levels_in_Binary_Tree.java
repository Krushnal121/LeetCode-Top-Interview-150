class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            int n = q.size();
            double ans = 0;
            for(int j = 0; j < n; ++j){
                TreeNode node = q.poll();
                ans += node.val;
                if(node.left != null)
                    q.add(node.left);
                if(node.right != null)
                    q.add(node.right);
            }
            res.add(ans / n);
        }
        return res;
    }
}