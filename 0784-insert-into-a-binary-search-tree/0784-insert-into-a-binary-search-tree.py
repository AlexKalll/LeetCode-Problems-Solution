# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        node = TreeNode(val)
        if not root:
            return node

        curr = root
        
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = node
                    return root
                curr = curr.left

            if val > curr.val:
                if not curr.right:
                    curr.right = node
                    return root
                curr = curr.right
        
        return 
"""
"""
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        def dfs(node, val):
            if node.val == val:
                return
            
            elif val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    dfs(node.left, val)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    dfs(node.right, val)

            return node
        
        return dfs(root, val)
    """

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = dfs(node.left, val)
            elif val > node.val:
                node.right = dfs(node.right, val)
            
            return node
        
        return dfs(root, val)