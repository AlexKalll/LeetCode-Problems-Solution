class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def backtrack(curr):
            if len(curr) == n:
                ans.append(''.join(curr[:]))
                return 

            for bit in '01':
                if curr and curr[-1] == '0' and bit == '0':
                    continue
                curr.append(bit)
                backtrack(curr)
                curr.pop()
        
        backtrack([])
        return ans