class Solution:
    def kLengthApart(self, a: List[int], k: int) -> bool:
        j = -inf
        return all(j+k<(j:=i) for i,v in enumerate(a) if v)