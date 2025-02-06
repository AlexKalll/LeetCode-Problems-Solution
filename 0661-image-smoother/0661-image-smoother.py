class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])

        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        ans = [[0]*cols for _ in range(rows)] 
        
        for i in range(rows):
            for j in range(cols):
                summ = img[i][j]
                count = 1
                for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1), (i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1)):
                    if is_inbound(x, y):
                        summ += img[x][y]
                        count += 1
                ans[i][j] = (summ//count)

        return ans

