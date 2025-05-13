class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for num in range(n+1):
            count = 0
            while num:
                mod = num & 1  # mod = num % 2
                count += mod == 1
                num >>= 1  # num = num // 2
            ans.append(count)

        return ans