# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inordersuccessor(node):
            while node.left:
                node = node.left
            
            return node

        def delete_node(node, key):
            if not node:
                return None
            
            if key < node.val:
                node.left = delete_node(node.left, key)
            elif key > node.val:
                node.right = delete_node(node.right, key)
            else:
                if not node.right:
                    return node.left
                elif not node.left:
                    return node.right

                successor = inordersuccessor(node.right)
                node.val = successor.val
                node.right = delete_node(node.right, successor.val)

            return node

        return delete_node(root, key)

        