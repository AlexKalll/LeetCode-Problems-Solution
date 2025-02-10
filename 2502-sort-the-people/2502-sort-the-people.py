class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # using selection sort 
        n = len(heights)

        for i in range(n):
            smallest = i

            for j in range(i+1, n):
                if heights[j] > heights[smallest]:
                    smallest = j

            heights[smallest], heights[i] = heights[i], heights[smallest]
            names[smallest], names[i] = names[i], names[smallest]

        return names