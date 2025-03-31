class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
            
        contributions = []

        for i in range(len(weights) - 1):
            contributions.append(weights[i] + weights[i + 1])
        
        contributions.sort()
        
        # min score: sum of k-1 smallest contributions
        min_score = sum(contributions[:k - 1])
        
        # max score: sum of k-1 largest contributions
        max_score = sum(contributions[-(k - 1):])
        
        return max_score - min_score
