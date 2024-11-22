class Solution:
    def inorder(self, root, ans):
        if not root:
            return

        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)

    def kthSmallest(self, root, k):
        ans = []
        self.inorder(root, ans)
        return ans[k - 1]