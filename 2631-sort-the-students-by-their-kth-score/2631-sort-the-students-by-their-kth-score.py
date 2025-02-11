class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        ht = defaultdict(list)
        
        for i in range(len(score)):
            ht[score[i][k]] = score[i]
        ht = dict(sorted(ht.items(), key =lambda x: x[0], reverse = True))
        
        return list(ht.values())
        