# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
                break
            slow = slow.next
        
        prev, curr, slow.next = None, slow.next, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        while head and prev:
            temp = head.next
            head.next = prev
            temp2 = prev.next
            prev.next = temp
            head = head.next.next
            prev = temp2
