class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        ans = [words[0]]
        for i in range(1, len(words)):
            w1 = Counter(ans[-1])
            w2 = Counter(words[i])

            if w1 != w2:
                ans.append(words[i])

        return ans