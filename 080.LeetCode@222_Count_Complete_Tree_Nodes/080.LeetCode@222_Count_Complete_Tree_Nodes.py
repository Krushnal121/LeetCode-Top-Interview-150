class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return 0 if not root else self.countNodes(root.left) + self.countNodes(root.right) + 1