class Solution:
    def maxIceCream(self, a: List[int], q: int) -> int:
        return bisect_right([*accumulate(sorted(a))],q)