class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # Find the index of the left child in postorder
        left_child_val = preorder[1]
        left_child_index = postorder.index(left_child_val)
        
        # Recursively construct the left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:left_child_index + 2], postorder[:left_child_index + 1])
        root.right = self.constructFromPrePost(preorder[left_child_index + 2:], postorder[left_child_index + 1:-1])
        
        return root
