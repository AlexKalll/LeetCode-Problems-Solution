# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        sum1 = l1.val + l2.val
        head = ListNode(sum1 % 10)
        dummy.next = head
        curr = head

        carry = sum1 // 10
        
        while l1 and l2 and l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            curr_sum =  l1.val + l2.val + carry
            carry = curr_sum // 10
            temp = ListNode(curr_sum % 10)
            curr.next = temp
            curr = curr.next
        
        while l1 and l1.next:
            l1 = l1.next
            curr_sum =  l1.val + carry
            carry = curr_sum // 10
            temp = ListNode(curr_sum % 10)
            curr.next = temp
            curr = curr.next
        
        while l2 and l2.next:
            l2 = l2.next
            curr_sum =  l2.val + carry
            carry = curr_sum // 10
            temp = ListNode(curr_sum % 10)
            curr.next = temp
            curr = curr.next
        
        if carry:
            curr.next = ListNode(1)
            
        return head
