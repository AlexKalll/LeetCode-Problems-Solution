class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        maxLen = length = 1

        flag = 0

        for i in range(len(arr) - 1):
            if (flag == 0 or flag == 2) and arr[i] > arr[i + 1]:
                flag = 1
                length += 1
                maxLen = max(maxLen, length)
            elif (flag == 0 or flag == 1) and arr[i] < arr[i + 1]:
                flag = 2
                length += 1
                maxLen = max(maxLen, length)
            else:
                if arr[i] == arr[i + 1]:
                    length = 1
                else:
                    length = 2

        return maxLen