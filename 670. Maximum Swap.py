class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num

        num = list(str(num))
        n = len(num)
        left, right, maxidx = -1, n-1, n-1
        for i in range(n-2, -1, -1):
            if num[i] > num[maxidx]:
                maxidx = i
            elif num[i] < num[maxidx]:
                right = maxidx
                left = i
        if left != -1:
            num[left], num[right] = num[right], num[left]

        return int(''.join(num))
