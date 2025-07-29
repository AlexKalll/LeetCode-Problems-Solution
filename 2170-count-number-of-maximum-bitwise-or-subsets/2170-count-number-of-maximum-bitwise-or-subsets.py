class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = []
        def backtrack(start, path):
            if path: # ths helps not to append the empty set 
                subsets.append(path.copy())
            for i in range(start, len(nums)):
                backtrack(i+1, path + [nums[i]])

        backtrack(0, [])

        max_bitwise = 0
        for num in nums:
            max_bitwise |= num

        count = 0
        for subset in subsets:
            curr = 0
            for num in subset:
                curr |= num
            
            if curr == max_bitwise:
                count += 1

        return count