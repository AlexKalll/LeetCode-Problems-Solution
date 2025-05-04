class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            count[key] += 1
        
        pairs = 0
        for c in count.values():
            pairs += c * (c - 1) // 2
        
        return pairs
