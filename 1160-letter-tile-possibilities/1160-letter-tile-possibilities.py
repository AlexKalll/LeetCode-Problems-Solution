class Solution(object):
    def numTilePossibilities(self, tiles):
        s=set()
        tiles=list(tiles)
        for i in range(1,len(tiles)+1):
            x=permutations(tiles,i)
            for i in x:
                s.add(i)
        return len(s)
        