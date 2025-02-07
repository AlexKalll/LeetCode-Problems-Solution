class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        # sort the dictionary based one the values in reverse order and return a list
        hT = sorted(nums_count.items(), key = lambda item: item[1], reverse = True)
        # changing it to a dictionary
        hT = dict(hT)

        ans = []
        i = 0
        for key in hT:
            if i >= k:
                break 

            ans.append(key)
            i += 1
        
        return ans 
