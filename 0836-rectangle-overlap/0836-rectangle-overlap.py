class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left1, right1 = min(rec1[0], rec1[2]), max(rec1[0], rec1[2])
        left2, right2 = min(rec2[0], rec2[2]), max(rec2[0], rec2[2])

        bottom1, top1 = min(rec1[1], rec1[3]), max(rec1[1], rec1[3])
        bottom2, top2 = min(rec2[1], rec2[3]), max(rec2[1], rec2[3])

        return not (
            right1 <= left2 or right2 <= left1 or
            top1 <= bottom2 or top2 <= bottom1
        )