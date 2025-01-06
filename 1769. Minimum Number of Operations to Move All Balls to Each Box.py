# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(boxes)
        prefix = [0]*len(boxes)
        balls = int(boxes[0])
        for i in range(1,len(boxes)):
            prefix[i] = prefix[i-1]+balls
            balls += int(boxes[i])

        balls = int(boxes[-1])
        suffix = [0]*len(boxes)
        for i in range(len(boxes)-2,-1,-1):
            suffix[i] = suffix[i+1]+balls
            balls += int(boxes[i])

        res = [0]*len(boxes)
        for i in range(len(res)):
            res[i] = prefix[i]+suffix[i]
            
        return res
