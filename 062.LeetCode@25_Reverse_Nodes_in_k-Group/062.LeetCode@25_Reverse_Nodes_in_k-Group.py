class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy

        while ptr is not None:
            tracker = ptr

            # Check if there are at least k nodes ahead
            for i in range(k):
                tracker = tracker.next
                if tracker is None:
                    return dummy.next

            # Reverse the k nodes
            previous, current = self.reverseLinkedList(ptr.next, k)

            # Link the reversed part back to the main list
            lastNodeOfReversedGroup = ptr.next
            lastNodeOfReversedGroup.next = current
            ptr.next = previous
            ptr = lastNodeOfReversedGroup

        return dummy.next

    def reverseLinkedList(self, head: ListNode, k: int) -> Tuple[ListNode, ListNode]:
        previous = None
        current = head

        for _ in range(k):
            # Temporarily store the next node
            next_node = current.next
            # Reverse the current node
            current.next = previous
            # Move previous and current one step forward
            previous = current
            current = next_node

        return previous, current