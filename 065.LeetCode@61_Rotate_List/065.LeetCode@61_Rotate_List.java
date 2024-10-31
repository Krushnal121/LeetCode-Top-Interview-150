class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0 || head.next == null) {
            return head;
        }
        ListNode temp = head;
        int count = 0;
        ListNode end= head;
        while (temp != null) {
            end = temp;
            temp = temp.next;
            count += 1;
        }
        if (count == k || (k % count == 0 && k != 1)) {
            return head;
        }
        temp = head;
        int loc = (count + k) % count;
        for (int i = 0; i < count - loc -1; i++) {
            temp = temp.next;
        }
        ListNode start = temp.next;
        temp.next = null;
        end.next = head;
        return start;
    }
}