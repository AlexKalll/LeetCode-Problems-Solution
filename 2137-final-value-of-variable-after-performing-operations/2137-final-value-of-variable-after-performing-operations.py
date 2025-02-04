class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        hT = Counter(operations)
        x = 0
        for op in hT:
            if op == '--X' or op == 'X--':
                x -= hT[op]
            else:
                x += hT[op]
        return x