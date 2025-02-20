# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using hare and tortoise or hash table approaches
        hare = head 
        tort = head 
        
        while hare and hare.next:
            hare = hare.next.next
            tort = tort.next
            if hare == tort:
               return True
        
        return False