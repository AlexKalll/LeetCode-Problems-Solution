# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, minval, maxval):
            if not node:
                return maxval - minval
            
            if node.val < minval:
                minval = node.val
            if node.val > maxval:
                maxval = node.val
            
            left_diff = dfs(node.left, minval, maxval)
            right_diff = dfs(node.right, minval, maxval)


            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)
