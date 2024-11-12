class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        return self.find(root, "")

    def find(self, root, a):
        if not root:
            return 0
        if not root.left and not root.right:
            return int(a + str(root.val))
        return self.find(root.left, a + str(root.val)) + self.find(root.right, a + str(root.val))