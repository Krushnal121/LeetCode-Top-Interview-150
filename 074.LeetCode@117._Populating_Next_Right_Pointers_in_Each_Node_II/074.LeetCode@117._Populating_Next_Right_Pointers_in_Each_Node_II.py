class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        head = root

        while head:
            temp = Node()
            cur = temp

            while head:
                if head.left:
                    cur.next = head.left
                    cur = cur.next

                if head.right:
                    cur.next = head.right
                    cur = cur.next

                head = head.next

            head = temp.next

        return root