class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        # sort the dictionary based one the values in reverse order and return a list
        hT = nums_count.most_common(k)
        ans = [key for key, val in hT]
        
        return ans
