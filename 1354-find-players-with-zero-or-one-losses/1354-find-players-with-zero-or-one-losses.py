class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_count = defaultdict(int)
        for w, l in matches:
            lose_count[w] += 0
            lose_count[l] += 1
        zero_lose = list(player for player in lose_count if lose_count[player]== 0)
        one_lose = [player for player in lose_count if lose_count[player]== 1]

        ans = [sorted(zero_lose), sorted(one_lose)]
        return ans
