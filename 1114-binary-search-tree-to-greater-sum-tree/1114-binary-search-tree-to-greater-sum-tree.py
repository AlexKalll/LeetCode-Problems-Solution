# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        curr = 0
        def helper(node):
            nonlocal curr
            if not node:
                return 
            
            helper(node.right)
            curr += node.val
            node.val = curr
            helper(node.left)
        
        helper(root)
        return root