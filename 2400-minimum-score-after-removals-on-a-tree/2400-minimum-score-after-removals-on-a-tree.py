class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        size = len(nums)                        # number of nodes
        tin = [0 for i in range(size)]          # tin[i] : time at which we entered in dfs for node i
        tout = [0 for i in range(size)]         # tout[i] : time at which we moved out from dfs for node i
        subXor = [0 for i in range(size)]       # subXor[i] : xor of the tree rooted at node i

        self.timer = 0

        # building adjacency list
        adjList = [[] for i in range(size)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        # DFS which visits entire tree, marks the timestamp of in & out, calculates the xor values at each node
        def dfs(node,parent):
            tin[node] = self.timer
            subXor[node] = nums[node]
            self.timer += 1
            for neigh in adjList[node]:
                if neigh == parent: # ignore parent
                    continue
                subXor[node] ^= dfs(neigh,node)
            tout[node] = self.timer
            return subXor[node]
        
        # assuming root is 0 and starting the traversal.
        totalXor = dfs(0,-1)

        
        orientedList = [] # represents a list of all the children nodes. suppose for edge u->v ( here, showing as directed as we have assumed that root is 0 so accordingly we can assume that coming downwards from 0, we can show this as directed edge ) : v will be counted as oriented node and will be captured in oriented list. so that when we are selecting the edge ( to remove ), we don't have to worry about which node to chose from. we'll simply choose the node from this list. as at each node we'll have a precalculated xor value - which we can easily use to count xor of different component. [ calculating xor of componenets through the parent xor of the nodes will induce ambuiguity and complexity in understanding. you can ask GPT to show some diagrams to visualize this approach ]


        def isAncestor(u,v): # returns true if u is an ancestor of v
            return tin[u] <= tin[v] < tout[u] # simple Euler‐tour timestamp (tin/tout) trick 

        # creating oriented list ( children nodes of all edges. ie. from edge u->v : it'll add v to oriented edge )
        for u,v in edges:
            if isAncestor(u,v):
                orientedList.append(v)
            else:
                orientedList.append(u)
        
        minimumScore = float('inf')

        def calculateScore(comp1,comp2,comp3):
            return max(comp1,comp2,comp3) - min(comp1,comp2,comp3)

        # iterating from our list to check components for each pair u,v ( ie we'll remove the edge above node u, and above node v ( as discussed they are the child node from each edge ). we'll have three componenets after removing two edges )
        for i in range(len(orientedList)):
            for j in range(i+1,len(orientedList)):
                u = orientedList[i]
                v = orientedList[j]


                # also here, we are making use of following XOR property extensively ( without that, I was clueless )
                # totalXor = x1 ^ x2 ^ x3
                # and we can rearrange that to x3 = x1 ^ x2 ^ totalXor and so on...

                if isAncestor(u,v): # if u is the ancestor of v
                    inner = subXor[v]
                    mid = subXor[u] ^ inner
                    outer = totalXor ^ subXor[u]
                    minimumScore = min(minimumScore, calculateScore(inner,mid,outer))
                elif isAncestor(v,u): # if v is the ancestor of u
                    inner = subXor[u]
                    mid = subXor[v] ^ inner
                    outer = totalXor ^ subXor[v]
                    minimumScore = min(minimumScore, calculateScore(inner,mid,outer))
                else: # else, both of them are in a different sub trees
                    inner1 = subXor[u]
                    inner2 = subXor[v]
                    outer = totalXor ^ subXor[u] ^ subXor[v]
                    minimumScore = min(minimumScore, calculateScore(inner1,inner2,outer))
                
        return minimumScore