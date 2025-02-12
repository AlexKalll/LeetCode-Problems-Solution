class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ht = defaultdict(list) # a hash map to  store two numbers that their digit sum is equal and these should be tha largests among all possibles

        for num in nums:
            curr = sum(list(map(int, str(num))))
            if curr not in ht:
                ht[curr] = [0, 0]
            
            if num > ht[curr][1]: 
                ht[curr][1] = num
                if ht[curr][1] > ht[curr][0]:
                    ht[curr][0], ht[curr][1] = ht[curr][1], ht[curr][0]
        ans = 0
        print(ht)
        for curr in ht:
            if ht[curr][0] > 0 and ht[curr][1] > 0:
                ans = max(ans, sum(ht[curr]))
        if ans:
            return ans 
        
        return -1