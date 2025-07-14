class Solution:#
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n = len(players)
        m = len(trainers)
        players.sort()
        trainers.sort()
        count = 0
        i, j = 0, 0

        while i < n and j < m:
            if  players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count 