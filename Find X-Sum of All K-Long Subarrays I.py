class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            count = Counter(subarray)
            print(count)

            # Sort the items by frequency and then by value
            print(count.items())
            sorted_items = sorted(count.items(), key=lambda pair: (-pair[1], -pair[0]))
            print(sorted_items)
            # Take the top x most frequent elements
            top_x = sorted_items[:x]
            
            # Calculate the x-sum
            x_sum = sum(value * freq for value, freq in top_x)
            answer.append(x_sum)
        
        return answer

"""
Example 1:
Counter({1: 2, 2: 2, 3: 1, 4: 1})
dict_items([(1, 2), (2, 2), (3, 1), (4, 1)])
[(2, 2), (1, 2), (4, 1), (3, 1)]
Counter({2: 3, 1: 1, 3: 1, 4: 1})
dict_items([(1, 1), (2, 3), (3, 1), (4, 1)])
[(2, 3), (4, 1), (3, 1), (1, 1)]
Counter({2: 3, 3: 2, 4: 1})
"""
