# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass approach
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        count = 0

        while curr:
            curr = curr.next 
            count += 1
        
        count2 = 0
        curr = dummy
        
        while count2 < count - n - 1:
            curr = curr.next
            count2 += 1
        
        if curr.next:
            curr.next = curr.next.next
   

        return dummy.next