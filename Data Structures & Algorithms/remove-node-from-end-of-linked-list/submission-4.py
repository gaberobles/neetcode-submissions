# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = head
        l = 0
        while h:
            l += 1
            h = h.next

        h, p = head, head
        
        if l-n == 0:
            if head.next:
                head = head.next
            else:
                return None
        else:
            for i in range(l-n):
                p = h
                h = h.next
            if h.next:
                p.next = h.next
            else:
                p.next = None


        return head