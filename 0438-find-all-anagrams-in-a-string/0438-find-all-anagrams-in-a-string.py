class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        k = len(p)
        p_count = Counter(p)
        curr_count = defaultdict(int)
        anagrams = []

        for i in range(k):
            curr_count[s[i]] += 1
        
        if curr_count == p_count:
            anagrams.append(0)
        
        for right in range(k, len(s)):
            curr_count[s[right-k]] -= 1 
            if curr_count[s[right-k]] == 0:
                del curr_count[s[right-k]]
            
            curr_count[s[right]] += 1

            if curr_count == p_count:
                anagrams.append(right-k+1) 

        return anagrams 