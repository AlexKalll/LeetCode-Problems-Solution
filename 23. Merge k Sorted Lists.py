# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_ = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_.append(self.helper(l1, l2)) 
            lists = merged_
        
        return lists[0] 

    def helper(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
# Time Complexity: O(N log k), where N is the total number of nodes across all lists. The merging of two lists takes O(N) time, and since we are merging k lists, it takes log k iterations.
# Space Complexity: O(1) for the merging process (in-place), but O(k) for the input lists if we consider the space used for the input.
