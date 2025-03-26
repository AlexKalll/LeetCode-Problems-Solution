class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def backtrack(curr):
            if len(curr) == len(nums):
                if ''.join(curr) not in nums:
                    return ''.join(curr)
                return ''

            for bit in '01':
                curr.append(bit)
                ans = backtrack(curr)
                if ans:
                    return ans
                curr.pop()

            return ''
        
        return backtrack([])