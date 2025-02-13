class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        k = len(s1)
        curr_count = defaultdict(int)

        for i in range(k):
            curr_count[s2[i]] += 1
        
        if curr_count == s1_count:
            return True
        
        for right in range(k, len(s2)):
            curr_count[s2[right]] += 1
            curr_count[s2[right-k]] -= 1
            if curr_count[s2[right-k]] == 0:
                del curr_count[s2[right-k]]
            
            if curr_count == s1_count:
                return True
        
        return False