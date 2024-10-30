class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if size == n:
            return head.next
        prev = head
        for _ in range(1, size - n):
            prev = prev.next
        prev.next = prev.next.next

        return head