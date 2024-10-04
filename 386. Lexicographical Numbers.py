"""
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 
Constraints:
1 <= n <= 5 * 10^4

Time: O(n)
Space: O(1) since the max call stack will be O(5) because in the constraint n <= 50000, i.e at most 5 digits which is constant 
"""

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(cur):
            if cur > n:
                return 
            ans.append(cur)
            cur *= 10  # everytime the number increases by 1 digit 
            for i in range(10): # not msd
                dfs(cur+i) # adding the reminder
            
        for i in range(1,10): # the most segnificat digits 
            dfs(i)
        
        return ans


# we can do this in iterative manner as well 
