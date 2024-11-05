class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or root.left==root.right:
            return root
        tempright = self.invertTree(root.left)
        templeft = self.invertTree(root.right)
        root.left = templeft
        root.right = tempright
        return root