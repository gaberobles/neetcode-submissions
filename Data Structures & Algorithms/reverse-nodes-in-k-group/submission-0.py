# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        while head:
            start = head
            for i in range(k):
                if head:
                    previous = head
                    head = head.next
                else:
                    print("broke!")
                    prevtail.next = start
                    return dummy

            prev, curr = None, start
            previous.next = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            if dummy.val == -1:
                dummy = prev
                prevtail = start
            else:
                prevtail.next = prev
                prevtail = start
            

        return dummy