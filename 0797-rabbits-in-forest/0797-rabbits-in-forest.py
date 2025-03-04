class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ht = Counter(answers)
        count = len(answers)
        
        for key in ht:
            same_color = key + 1 
            rem = ht[key] % (same_color)
            if rem:
                count += same_color - rem

        return count