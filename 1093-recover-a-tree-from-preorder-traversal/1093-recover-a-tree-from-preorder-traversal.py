class Solution:
    def recoverFromPreorder(self, data):
        # Replace dashes with corresponding characters
        for count in range(100, 0, -1):
            data = data.replace("-" * count, chr(count + 65))

        def build_tree(parts, level):
            # aplit parts based on the current level character
            parts = parts.split(chr(level + 65))
            
            node = TreeNode(int(parts[0]))
            
            # recursively build left subtree
            if len(parts) > 1:
                node.left = build_tree(parts[1], level + 1)
            else:
                node.left = None
            
            # build right subtree
            if len(parts) > 2:
                node.right = build_tree(parts[2], level + 1)
            else:
                node.right = None
            
            return node

        return build_tree(data, 1)
