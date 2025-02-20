# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tort = hare = head

        is_cycled = False
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next

            if hare == tort:
                is_cycled = True
                break

        if is_cycled:
            tort = head 
            
            while tort != hare:
                hare = hare.next
                tort = tort.next
            
            return hare

    
        return 