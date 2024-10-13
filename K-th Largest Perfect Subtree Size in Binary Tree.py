# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_size = dfs(node.left)
            right_size = dfs(node.right)
            
            # Check if both children are perfect and have the same size
            if left_size == right_size and (left_size > 0 or (node.left is None and node.right is None)):
                size = left_size + right_size + 1
                sizes.append(size)
                return size
            
            return 0
        
        dfs(root)
        
        # Sort sizes in descending order
        sizes.sort(reverse=True)
        
        # Return the k-th largest size or -1 if it doesn't exist
        return sizes[k - 1] if k <= len(sizes) else -1
"""
Explanation:
Single Function: The kthLargestPerfectSubtree method contains the logic to both check for perfect binary subtrees and collect their sizes.
Depth-First Search (DFS): The dfs function traverses the tree recursively:
It calculates the sizes of the left and right subtrees.
It checks if both subtrees are perfect and have the same size.
If they are, it adds the size of the current perfect binary subtree to the sizes list.
Sorting and Returning: After collecting sizes, the sizes are sorted in descending order, and the k-th largest size is returned, or -1 if there are not enough perfect subtrees. """
