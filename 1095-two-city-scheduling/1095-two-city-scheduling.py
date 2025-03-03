class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key = lambda x:(x[0] -x[1]))
        
        print(costs)
        
        min_cost = 0
        for i in range(n):
            if i < n//2:
                min_cost += costs[i][0]
        
            else:
                min_cost += costs[i][1]

        return min_cost