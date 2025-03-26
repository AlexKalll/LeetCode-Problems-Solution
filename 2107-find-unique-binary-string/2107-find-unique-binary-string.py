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