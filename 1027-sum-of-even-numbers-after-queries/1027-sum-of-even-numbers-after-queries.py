class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        hT = defaultdict(int)
        curr = 0
        for i, num in enumerate(nums):
            if num % 2 == 0:
                curr += num

            hT[i] = num
                
        ans = []
        for val, i in queries:
            if hT[i] % 2 == 0:
                if val % 2 == 0:
                    curr += val
                else:
                    curr -= hT[i]
            else:
                if val % 2 == 1:
                    curr += (hT[i] + val)
                    
            hT[i] += val
            ans.append(curr)

        return ans 
                    
