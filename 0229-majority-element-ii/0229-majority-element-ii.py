class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        left = 0
        ans = []

        for r in range(n):
            if nums[left] != nums[r]:
                if r - left > n//3:
                    ans.append(nums[left])
                left = r # update l pointer if nums[l] and nums[r] aren't same
        # if the last more than n//3 elements are the same, this case checks since we are updating left when nums at pointers are different
        if n - left > n//3:
            ans.append(nums[-1]) 

        return ans 