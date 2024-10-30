class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size=0;
        ListNode temp=head;
        while(temp!=null){
            size++;
            temp=temp.next;
        }
        if(size==n){
            head=head.next;
            return head;
        }
        ListNode prev=head;
        int i=1;
        while(i<(size-n)){
            prev=prev.next;
            i++;
        }
        prev.next=prev.next.next;
        return head;
    }
}