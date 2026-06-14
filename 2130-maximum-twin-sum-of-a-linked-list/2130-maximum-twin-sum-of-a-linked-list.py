# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        right = slow 
        while right:
            next_node = right.next
            right.next = prev
            prev = right
            right = next_node
            
        right = prev
        left = head
        max_sum = 0
        
        while right:
            curr_sum = left.val + right.val
            max_sum = max(max_sum, curr_sum)
            
            left = left.next
            right = right.next

        return max_sum