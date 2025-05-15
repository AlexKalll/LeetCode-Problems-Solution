class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        result.append(words[0])
        
        for i in range(1, len(words)):
            if groups[i] != groups[words.index(result[-1])]:
                result.append(words[i])
        
        return result