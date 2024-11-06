class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_set_bits(n1, n2):
            return bin(n1).count('1') == bin(n2).count("1")
        
        for _ in range(len(nums)):
            for i in range(1, len(nums)):
                if count_set_bits(nums[i-1], nums[i]):
                    if nums[i-1] > nums[i]:
                        nums[i-1], nums[i] = nums[i], nums[i-1]
                else:
                    if nums[i-1] > nums[i]:
                        return False

        return nums == sorted(nums)
