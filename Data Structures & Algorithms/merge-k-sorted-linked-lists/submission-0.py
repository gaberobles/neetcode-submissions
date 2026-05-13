# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        for i in range(len(lists)):
            print(lists[i].val)
        while lists:
            min = 1001
            minIndex = -1
            for i, h in enumerate(lists):
                if h:
                    if h.val < min:
                        print("new min: ", i, h.val)
                        min = h.val
                        minIndex = i
            if minIndex != -1:
                print("appending value: ", lists[minIndex].val)
                head.next = lists[minIndex]
                head = head.next
                lists[minIndex] = lists[minIndex].next
            for i, h in enumerate(lists):
                if not h:
                    del lists[i]
        return dummy.next