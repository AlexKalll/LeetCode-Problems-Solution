class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pref = [0] * n
        ans = 0

        for start, end in requests:
            pref[start] += 1
            if end + 1 < n:
                pref[end+1] -= 1
            
        for i in range(1, len(pref)):
            pref[i] += pref[i-1]

        pref.sort(reverse = True)
        nums.sort(reverse = True)

        for i in range(n):
            if pref[i] == 0:
                break
            ans += (nums[i] * pref[i])

        return ans % (10**9 + 7)
