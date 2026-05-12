"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        hash = {}
        i = 0

        curr = head
        while curr:
            copy = Node(curr.val)
            hash[curr] = copy
            curr = curr.next
            i += 1
        
        i = 1
        curr, copy = head, hash[head]
        while curr:
            copy.next = hash[curr.next] if curr.next else None
            copy.random = hash[curr.random] if curr.random else None
            copy, curr = copy.next, curr.next
            i += 1

        return hash[head]