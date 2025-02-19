# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # One pass -> using two pointer approach
        dummyNode = ListNode()
        dummyNode.next = head 

        prev = cur = dummyNode
        for i in range(n):
            cur = cur.next

        while cur.next:
            prev = prev.next
            cur = cur.next
        
        prev.next = prev.next.next

        return dummyNode.next