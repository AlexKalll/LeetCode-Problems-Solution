class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        root = {}
        size = {}

        # Find with path compression
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        # Union by size
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]

        for num in nums:
            root[num] = num
            size[num] = 1

        for num in nums:
            if num + 1 in root:
                union(num, num + 1)

        return max(size.values())
