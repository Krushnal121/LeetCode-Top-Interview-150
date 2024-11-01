class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_dummy = ListNode(0)
        less_tail = less_dummy

        greater_dummy = ListNode(0)
        greater_tail = greater_dummy

        current = head

        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
            current = current.next

        greater_tail.next = None

        less_tail.next = greater_dummy.next

        return less_dummy.next