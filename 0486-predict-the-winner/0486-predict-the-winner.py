class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        def helper(start, end):
            if start == end:
                return nums[start]

            choice1 = nums[start] - helper(start + 1, end)
            choice2 = nums[end] - helper(start, end - 1)

            return max(choice1, choice2)

        res = helper(0, n-1)

        return res >= 0
"""
explanation:
base case: when jst one unselected num remains, returns it and terminates teh recursion
choice1: when player1 selects at start, then p2 plays optimally as well
choice2: when player1 selects at end, then p2 plays optimally as well
finally, after all the possible case return the max of the two so that player1 will play optimally

return: player1 wins or in a tie

time complexity: O(2^n) since we are doing recursive call for choice1 and choice2
space: O(n)
"""
