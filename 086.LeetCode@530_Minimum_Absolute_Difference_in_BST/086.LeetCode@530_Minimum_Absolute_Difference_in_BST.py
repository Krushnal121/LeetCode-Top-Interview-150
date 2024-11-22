class Solution:
    def __init__(self):
        self.min = float('inf')
        self.prev = float('inf')

    def help(self, root):
        if root is None:
            return
        self.help(root.left)
        self.min = min(self.min, abs(root.val - self.prev))
        self.prev = root.val
        self.help(root.right)

    def getMinimumDifference(self, root):
        self.help(root)
        return self.min