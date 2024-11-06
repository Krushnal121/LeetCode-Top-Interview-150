class Solution:
    def isSymmetric(self, root: [TreeNode]):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)