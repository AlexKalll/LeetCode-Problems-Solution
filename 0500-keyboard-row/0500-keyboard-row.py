class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'

        ans = []
        for word in words:
            chars = Counter(word.lower())
            cnt1 = cnt2 = cnt3 = 0
            for c in chars:
                if c in row1:
                    cnt1 += 1
                elif c in row2:
                    cnt2 += 1
                else:
                    cnt3 += 1
            n = len(chars)
            if cnt1 == n or cnt2 == n or cnt3 == n:
                ans.append(word)
            
        return ans

                