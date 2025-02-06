class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            # Flip the row horizontally
            image[i] = image[i][::-1]
            # Invert the row
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]
                
        return image