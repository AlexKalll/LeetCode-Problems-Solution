class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mon_inc = deque()
        mon_dec = deque()

        ans = 0
        l  = 0
        for r in range(len(nums)):
            while mon_inc and nums[r] < nums[mon_inc[-1]]:
                mon_inc.pop()

            while mon_dec and nums[r] > nums[mon_dec[-1]]:
                mon_dec.pop()

            mon_inc.append(r)
            mon_dec.append(r)

            while nums[mon_dec[0]] - nums[mon_inc[0]] > limit:
                if nums[l] == nums[mon_dec[0]]:
                    mon_dec.popleft()
                elif nums[l] == nums[mon_inc[0]]:
                    mon_inc.popleft()
                
                l += 1
            ans = max(ans, r-l+1)

        return ans 