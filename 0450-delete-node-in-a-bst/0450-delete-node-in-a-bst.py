# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inordersuccessor(node):
            current = node
            while current.left:
                current = current.left
            return current

        def delete_node(node, key):
            if not node:
                return None
            
            if key < node.val:
                node.left = delete_node(node.left, key)
            elif key > node.val:
                node.right = delete_node(node.right, key)
            else:
                # Node with only one child or no child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                # Node with two children: Get the inorder successor
                successor = inordersuccessor(node.right)
                node.val = successor.val  # Copy the inorder successor's value to this node
                node.right = delete_node(node.right, successor.val)  # Delete the inorder successor
            
            return node

        return delete_node(root, key)