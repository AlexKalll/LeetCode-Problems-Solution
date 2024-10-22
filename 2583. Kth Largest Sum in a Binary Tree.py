# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        pos = []
        while q:
            n = len(q)
            lsum = 0

            for _ in range(n):
                node = q.popleft()
                lsum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)         
            pos.append(lsum)

        if k <= len(pos):
            pos.sort() 
            return pos[-k]

        return -1
