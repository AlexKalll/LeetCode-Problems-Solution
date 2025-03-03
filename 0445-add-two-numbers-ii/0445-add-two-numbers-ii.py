# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        st1 = []
        st2 = []
        
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        prev = None
        while st1 and st2:
            summ = st1.pop() + st2.pop() + carry
            carry = summ // 10
            curr = ListNode(summ%10)
            curr.next = prev 
            prev = curr

        while st1:
            summ = st1.pop() + carry
            carry = summ // 10
            curr = ListNode(summ%10)
            curr.next = prev 
            prev = curr
        
        while st2:
            summ = st2.pop() + carry
            carry = summ // 10
            curr = ListNode(summ%10)
            curr.next = prev 
            prev = curr
        
        if carry:
            curr = ListNode(carry)
            curr.next = prev
        
        return curr
        """
        def push_to_stack(node):
            stack = []
            while node:
                stack.append(node.val)
                node = node.next
            return stack
        
        stack1 = push_to_stack(l1)
        stack2 = push_to_stack(l2)
        
        carry = 0
        prev = None
        
        while stack1 or stack2 or carry:
            total = carry
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
                
            carry = total // 10
            curr = ListNode(total % 10)
            curr.next = prev
            prev = curr
        
        return prev