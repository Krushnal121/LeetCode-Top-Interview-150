class Solution:
    def isValidBST(self, root):
        return self.helper(root, None, None)

    def helper(self, root, min_node, max_node):
        if root is None:
            return True
        if min_node is not None and root.val <= min_node.val:
            return False
        if max_node is not None and root.val >= max_node.val:
            return False
        return self.helper(root.left, min_node, root) and self.helper(root.right, root, max_node)