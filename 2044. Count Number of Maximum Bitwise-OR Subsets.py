class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = []
        #In the worst case, the time taken to generate all subsets is O(2^n)
        def backtrack(start, path):
            if path: # this helps not to append the empty set 
                subsets.append(path.copy())
                print(path)
                # print(subsets)
            for i in range(start, len(nums)):
                backtrack(i+1, path + [nums[i]])

        backtrack(0, [])

        max_bitwise = 0
        for num in nums: #since the bitwise or of all elements is the max one with O(n) time 
            max_bitwise |= num 

        count = 0
        for subset in subsets: # O(2^n)
            curr = 0
            for num in subset: #O(n)
                curr |= num
            
            if curr == max_bitwise:
                count += 1

        return count

# overall time is O(n+2^n+ n*2^n) i.e. O(n*2^n) since we will choose the upper bound 
# space complexity is (2^n) for storing the subsets.
