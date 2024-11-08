class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        merge = ""
        p1, p2 = 0, 0

        while p1 < n1 and p2 < n2:
            if word1[p1:] > word2[p2:]:
                merge += word1[p1]
                p1 += 1
            else:
                merge += word2[p2]
                p2 += 1

        merge += word1[p1:] + word2[p2:]
        return merge
