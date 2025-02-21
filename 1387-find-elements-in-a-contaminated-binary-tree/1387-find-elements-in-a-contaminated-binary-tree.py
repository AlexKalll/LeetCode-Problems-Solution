# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.recovered_nodes = set()
        self.q = deque([])
        
        self.bfs(self.root, 0)
    # using bfs 
    def bfs(self, node, val):
        if not node:
            return 
        self.recovered_nodes.add(0) # initially 0 since it is guaranteed 
        node.val = val
        self.q.append(node)

        while self.q:
            node = self.q.popleft()
            curr_val = node.val
            if node.left:
                self.q.append(node.left)
                node.left.val = 2*curr_val + 1
                self.recovered_nodes.add(node.left.val)
            if node.right:
                self.q.append(node.right)
                node.right.val = 2*curr_val + 2
                self.recovered_nodes.add(node.right.val)

    def find(self, target: int) -> bool:
        
        return target in self.recovered_nodes

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

"""
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root 
        self.node_values = set()
        
        self.dfs(self.root, 0)

    def dfs(self, node, val):
        if not node:
            return 
        self.node_values.add(val)
        self.dfs(node.left, val*2 + 1)
        self.dfs(node.right, val*2 + 2)

    def find(self, target: int) -> bool:
        
        return (target in self.node_values)

"""