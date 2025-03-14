# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left) + 1
            right = helper(node.right) + 1

            return max(left, right)
        
        return helper(root)