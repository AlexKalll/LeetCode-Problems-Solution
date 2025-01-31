# https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.extend(list(int(n)for n in str(num)))

        return ans 
