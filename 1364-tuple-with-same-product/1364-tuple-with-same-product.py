class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                curr = nums[i] * nums[j]

                if curr in product:
                    ans += 8 * product[curr]

                product[curr] += 1

        return ans