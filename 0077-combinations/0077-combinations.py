class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [num for num in range(1, n+1)]
        
        combs = combinations(arr, k)
        ans = []
        
        for comb in combs:
            ans.append(list(comb))
        
        return ans