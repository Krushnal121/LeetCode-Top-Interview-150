class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1)
            return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode ptr = dummy;

        while (ptr != null) {
            ListNode tracker = ptr;

            for (int i = 0; i < k && tracker != null; i++) {
                tracker = tracker.next;
            }

            if (tracker == null) {
                break;
            }

            ListNode[] updatedNodes = reverseLinkedList(ptr.next, k);

            ListNode previous = updatedNodes[0];
            ListNode current = updatedNodes[1];

            ListNode lastNodeOfReversedGroup = ptr.next;
            lastNodeOfReversedGroup.next = current;
            ptr.next = previous;
            ptr = lastNodeOfReversedGroup;
        }

        return dummy.next;
    }

    private ListNode[] reverseLinkedList(ListNode head, int k) {
        ListNode previous = null;
        ListNode current = head;
        ListNode next = null;

        for (int i = 0; i < k; i++) {

            next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }

        return new ListNode[]{previous, current};
    }
}