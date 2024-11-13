class Solution:

    def traverse(self, node, storer):
        if not node:
            return 0
        left = self.traverse(node.left, storer)
        right = self.traverse(node.right, storer)
        if left<0:
            left = 0
        if right < 0:
            right = 0
        storer.append(left + right + node.val)
        return max(left,right) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxStorer = []
        self.traverse(root, maxStorer)
        return max(maxStorer)
