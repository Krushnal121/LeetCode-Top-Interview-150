class Solution:
    def rotateRight(self, head, k: int):
        if not head or k == 0 or not head.next:
            return head
        temp = head
        count = 0
        while temp is not None:
            if temp.next is not None:
                temp = temp.next
                count += 1
            else:
                end = temp
                count += 1
                break
        if count == k or (k % count == 0 and k != 1):
            return head
        temp = head
        loc = (count + k) % count
        for i in range(count - loc - 1):
            temp = temp.next
        start = temp.next
        temp.next = None
        end.next = head
        return start