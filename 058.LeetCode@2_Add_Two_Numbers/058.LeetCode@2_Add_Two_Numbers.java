class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head=l1;
        ListNode prev=null;
        int carry=0;
        while(l1!=null && l2!=null){
            int sum=l1.val+l2.val+carry;
            prev=l1;
            carry=0;
            if (sum>=10){
                l1.val=sum%10;
                carry=1;
            }
            else{
                l1.val=sum;
            }
            l1=l1.next;
            l2=l2.next;
        }
        while(l1!=null){
            int sum=l1.val+carry;
            prev=l1;
            carry=0;
            if (sum>=10){
                l1.val=sum%10;
                carry=1;
            }
            else{
                l1.val=sum;
            }
            l1=l1.next;
        }
        if(l2!=null){
            prev.next=l2;
        }
        while(l2!=null){
            int sum=l2.val+carry;
            prev=l2;
            carry=0;
            if (sum>=10){
                l2.val=sum%10;
                carry=1;
            }
            else{
                l2.val=sum;
            }
            l2=l2.next;
        }
        if(carry!=0){
            ListNode end=new ListNode(carry, null);
            prev.next=end;
        }
        return head;
    }
}