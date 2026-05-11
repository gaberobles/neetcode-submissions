# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def solve(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return 
            if node.next is None:
                return node
            else:
                newHead = solve(node.next)

                node.next.next = node
                node.next = None

                return newHead
                
        return solve(head)