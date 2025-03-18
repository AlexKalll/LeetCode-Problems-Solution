# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            if node.val == p or node.val == q:
                return node

            if (node.val > p and node.val < q) or (node.val < p and node.val > q):
                return node
            
            if node.val > p and node.val > q:
                return dfs(node.left, p, q)
            if node.val < p and node.val < q:
                return dfs(node.right, p, q)
            

        return dfs(root, p.val, q.val)