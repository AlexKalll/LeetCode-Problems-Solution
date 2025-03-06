class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        ht = defaultdict(int)
        ans = []
        for i in range(n):     
            for j in range(n):
                ht[grid[i][j]] += 1
                if ht[grid[i][j]] == 2:
                    ans.append(grid[i][j]) 
     
        for num in range(1, n**2 + 1):
            if num not in ht:
                ans.append(num)
                break
    
        return ans