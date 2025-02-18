class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        nums.sort()
        ht = defaultdict(list) 
        
        for num in nums:
            curr_sum = sum(map(int, list(str(num))))
            ht[curr_sum].append(num)

        ans = 0

        for key in ht:
            if len(ht[key]) >= 2:
                curr_ans = ht[key].pop() + ht[key].pop()
                ans = max(ans, curr_ans)
        
        if ans:
            return ans 
        
        return -1