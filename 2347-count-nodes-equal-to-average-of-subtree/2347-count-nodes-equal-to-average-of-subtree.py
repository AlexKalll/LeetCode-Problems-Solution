# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def dfs(node):
            nonlocal ans
            if not node:
                return (0, 0)

            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)
            
            curr_total = node.val + left_sum + right_sum
            curr_cnt = 1 + left_cnt + right_cnt
            avg = (curr_total) // (curr_cnt)

            if avg == node.val:
                ans += 1
            
            return (curr_total, curr_cnt)

        ans = 0 
        dfs(root)
        return ans 