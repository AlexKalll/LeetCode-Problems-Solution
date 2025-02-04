class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = []
        for num in cnt:
            if cnt[num] == 2:
                ans.append(num)

        return ans