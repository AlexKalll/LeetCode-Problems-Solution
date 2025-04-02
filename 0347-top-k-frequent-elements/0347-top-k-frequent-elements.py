class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = Counter(nums)
        m = max(ht.values())

        buckets = [[] for _ in range(m + 1)]

        for num in nums:
            idx = ht[num]
            buckets[idx].append(num)

        ans = []
        
        for bucket in reversed(buckets):
            if len(ans) == k:
                break
            bucket = set(bucket)
            for num in bucket:
                if len(ans) < k:
                    ans.append(num)
                else: 
                    break
            
        return ans