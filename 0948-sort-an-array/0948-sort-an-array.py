class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half, right_half):
            l = r = 0
            merged = []
            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    merged.append(left_half[l])
                    l += 1
                else:
                    merged.append(right_half[r])
                    r += 1
            merged.extend(left_half[l:])
            merged.extend(right_half[r:])

            return merged

        def mergeSort(left, right):
            if left == right:
                return [nums[left]]
            mid = (left + right) // 2
            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid+1, right)

            return merge(left_half, right_half)
        
        return mergeSort(0, len(nums)-1)
            