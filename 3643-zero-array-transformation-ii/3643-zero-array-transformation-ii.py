class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        sum_val = 0
        k = 0
        diff_arr = [0] * (n + 1)

        for i in range(n):
            while sum_val + diff_arr[i] < nums[i]:
                k += 1
                if k > len(queries):
                    return -1

                left, right, val = queries[k-1]

                if right >= i:
                    diff_arr[max(left, i)] += val

                    if right + 1 < len(diff_arr):
                        diff_arr[right + 1] -= val

            sum_val += diff_arr[i]

        # print(diff_arr)
        return k