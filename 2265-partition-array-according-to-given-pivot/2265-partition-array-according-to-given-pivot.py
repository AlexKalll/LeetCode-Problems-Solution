class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        cnt = 0

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                cnt += 1

        return less + [pivot] * cnt + greater