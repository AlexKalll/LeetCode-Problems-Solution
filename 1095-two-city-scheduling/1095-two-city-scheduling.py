class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        # we are gonna sort by the cost we gain or lost if we send a guy to city b i.e a-b if the more the -ve it should go to a 
        costs.sort(key = lambda x:(x[0] - x[1]))
        
        print(costs)
        
        min_cost = 0
        for i in range(n):
            if i < n//2:
                min_cost += costs[i][0]
        
            else:
                min_cost += costs[i][1]

        return min_cost