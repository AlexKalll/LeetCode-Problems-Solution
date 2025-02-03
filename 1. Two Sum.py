# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hT = defaultdict(list)
        
        for i, val in enumerate(nums):
            hT[val].append(i)
        print(hT)
        for val in hT:
            diff = target - val
            if diff in hT and diff != val:
                return [hT[val][0], hT[diff][0]]
            elif diff in hT and diff == val and len(hT[val]) > 1:
                return [hT[val][0], hT[val][1]]
