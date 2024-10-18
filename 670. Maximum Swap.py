"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.
 
Constraints:
0 <= num <= 10^8
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num

        num = list(str(num))
        n = len(num)
        left, right, maxidx = -1, n-1, n-1
        for i in range(n-2, -1, -1):
            if num[i] > num[maxidx]:
                maxidx = i
            elif num[i] < num[maxidx]:
                right = maxidx
                left = i
        if left != -1:
            num[left], num[right] = num[right], num[left]

        return int(''.join(num))
