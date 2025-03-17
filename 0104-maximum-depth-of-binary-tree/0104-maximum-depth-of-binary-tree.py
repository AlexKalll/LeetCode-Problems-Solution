# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left) 
            right = helper(node.right)

            return max(left, right) + 1
        
        return helper(root) 
"""
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 1

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth

"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            level_len = len(q)
            depth += 1
            for i in range(level_len):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return depth