"""
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                if ''.join(curr) not in nums:
                    return True

                return False

            for bit in '01':
                curr.append(bit)
                if backtrack(curr):
                    return ''.join(curr)
                curr.pop()

            return ''
        
        return backtrack([])
        """

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set(nums)

        for i in range(2**n):
            bini = bin(i)[2:]
            k = len(bini)
            curr =  '0' * (n-k) + bini
            
            if curr not in seen:
                return curr
        
        return 