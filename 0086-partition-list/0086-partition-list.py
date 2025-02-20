# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if x < -100 or not head:
            return 
        
        left = ListNode()  
        right = ListNode()
        # two dummy nodes: left_head and right_head
        left_head = left
        right_head = right

        curr = head 
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            
            curr = curr.next

        right.next = None
        left.next = right_head.next
    
        return left_head.next

