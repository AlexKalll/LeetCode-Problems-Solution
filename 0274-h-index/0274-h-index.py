class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse = True)

        count = 0
  

        for i, val in enumerate(citations):
            if val >= i + 1:
                count += 1        
            else:     
                break

        return count
