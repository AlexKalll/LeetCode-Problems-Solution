# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Initialize the result array with -1
        stack = []  # This will store the indices of the elements

        # Traverse the array twice to simulate the circular behavior
        for i in range(2 * n):
            # Use modulo to get the index in the original array
            current_index = i % n
            while stack and nums[stack[-1]] < nums[current_index]:
                # Pop the index from the stack and set the result
                index = stack.pop()
                result[index] = nums[current_index]
            if i < n:  # Only add the index for the first traversal
                stack.append(current_index)

        return result
