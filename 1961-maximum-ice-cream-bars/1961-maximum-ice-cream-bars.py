class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        M = max(costs)
        m = min(costs) # offset
        width = M - m + 1
        
        count = [0] * width 

        for cost in costs:
            count[cost-m] += 1

        creams = 0

        for i in range(len(count)):
            if coins >= count[i] * (i + m) and count[i] != 0:    
                creams += count[i]
                coins -= count[i] * (i+m)

            else:
                while coins >= (i + m) and count[i] != 0:
                    creams += 1
                    coins -= (i + m)
                    
        
        return creams 