class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        # Calculate the total sum of the first k cards
        total = sum(cardPoints[:k])
        max_score = total
        
        # Use a sliding window to consider taking cards from the end
        for i in range(1, k + 1):
            total = total - cardPoints[k - i] + cardPoints[n - i]
            max_score = max(max_score, total)
        
        return max_score