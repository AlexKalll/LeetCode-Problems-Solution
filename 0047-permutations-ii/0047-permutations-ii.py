class Solution:##
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [] 

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                ans.append(list(comb))
                return 

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1
                    
        backtrack([], Counter(nums))
        return ans