class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        cur = blocks[:k].count('W')
        print(cur)
        ops = float('inf')
        # update operations to count of W of initial window size k
        ops = cur
        # iterate througn bloacks from start to end of it
        for i in range(1, n-k+1):
            # remove the block going out of the window 
            if blocks[i-1] == 'W':
                cur -= 1
            # add a block coming into the windos
            if blocks[i+k-1] == 'W':
                cur += 1
            # finding the minimum operations
            ops = min(ops, cur)

        return ops 
