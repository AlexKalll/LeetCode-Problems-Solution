class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num2_xor = 0
        is_ln2_odd = len(nums2)%2
        is_ln1_odd = len(nums1)%2
        if is_ln1_odd:
            for i in nums2:
                num2_xor ^= i
        if is_ln2_odd:
            for i in nums1:
                num2_xor ^= i
        return num2_xor