class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]

        for index in range(1, len(words)):
            current = words[index]
            prev = words[index - 1]

            if sorted(current) != sorted(prev):
                ans.append(current)
        
        return ans