class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ht1 = defaultdict(int) # a hashmap to store ball:color pairs
        ht2 = defaultdict(int) # a hashmap  to store color:# of balls pairs

        ans = []
        for x, y in queries:
            if x in ht1:
                ht2[ht1[x]] -= 1
                if ht2[ht1[x]] == 0:
                    del ht2[ht1[x]]

            ht1[x] = y
            ht2[y] += 1

            ans.append(len(ht2))
        
        return ans