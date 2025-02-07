class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        # if n is mul of 4, I will lose the game since my fren play the game optimally 
                