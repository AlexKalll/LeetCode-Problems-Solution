# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(node, val):
            if not node:
                return None
                
            if val == node.val:
                return node

            elif val < node.val:
                return dfs(node.left, val)
            else:
                return dfs(node.right, val)
        
        return helper(root, val)
            
"""
# BFS approach 
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return None