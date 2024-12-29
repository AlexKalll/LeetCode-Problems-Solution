# https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, num1: List[int], num2: List[int]) -> List[int]:
        ans = []
        for num in num1:
            idx = num2.index(num)

            for i in range(idx + 1, len(num2)):
                if num2[i] > num:
                    ans.append(num2[i])
                    break
            else:
                ans.append(-1)

        return ans

""""
# stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to hold the next greater element for each number
        next_greater = {}
        stack = []
        
        # Iterate over nums2 to fill the next_greater dictionary
        for num in nums2:
            # Maintain elements in decreasing order in the stack
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # For numbers still in the stack, no greater element exists
        while stack:
            next_greater[stack.pop()] = -1
        
        # Generate results for nums1 based on the next_greater mapping
        result = [next_greater[num] for num in nums1]
        return result
"""
