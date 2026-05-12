# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i, j = l1, l2
        head = ListNode(0)

        remain = 0
        prev, curr = head, None
        while i and j:
            curr = ListNode((i.val + j.val + remain)%10)
            remain = (i.val + j.val)//10
            prev.next = curr
            prev = prev.next
            i, j = i.next, j.next

        if i:
            while i:
                curr = ListNode((i.val + remain)%10)
                remain = (i.val + remain)//10
                prev.next = curr
                prev = prev.next
                i = i.next

        elif j:
            while j:
                curr = ListNode((j.val + remain)%10)
                remain = (j.val + remain)//10
                prev.next = curr
                prev = prev.next
                j = j.next
        
        if remain:
            curr = ListNode(1)
            prev.next = curr

        return head.next