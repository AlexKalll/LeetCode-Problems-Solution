class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        cnt = -float('inf')
        ans = [0, 0]

        for i, row in enumerate(mat):
            curr = row.count(1)
            if curr > cnt:
                cnt = curr
                ans[0] = i
                ans[1] = cnt
        
        return ans 

