class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        player = [a for a in range(1, n+1)]

        def helper(player, cur):
            

            if len(player) == 1:
                return player[0]

            cur = (cur + k -1) % len(player)
            player.pop(cur)
            
            return helper(player, cur)
            
        return helper(player, 0)
