class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        current = root
        while current is not None:

            if current.left is not None:
                last = current.left
                while last.right is not None:
                    last = last.right

                last.right = current.right
                current.right = current.left
                current.left = None

            current = current.right