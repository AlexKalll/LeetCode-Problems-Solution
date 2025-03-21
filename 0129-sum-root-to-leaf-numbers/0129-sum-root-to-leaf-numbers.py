# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr):
            nonlocal ans
            if not node:
                return 
            
            # curr = curr * 10 + node.val

            if not node.left and not node.right:
                ans += curr
                return 

            arr = [node.left, node.right]
            for child in arr:
                if not child:
                    continue
                curr = curr * 10
                curr += child.val
                dfs(child, curr)
                curr -= child.val
                curr //= 10

        ans = 0
        dfs(root, root.val)
        return ans
            
