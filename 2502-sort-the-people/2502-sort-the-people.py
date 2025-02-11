"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #using bubble sort 
        n = len(heights)

        for i in range(n):
            swapped = False

            for j in range(1, n-i):
                if heights[j] > heights[j-1]:
                    heights[j], heights[j-1] = heights[j-1], heights[j]
                    names[j], names[j-1] = names[j-1], names[j]
                    swapped = True

            if not swapped:
                break
                
        return names
"""
"""
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
"""
# usinng insertion sort 
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)

        for i in range(1, n):
            key_height = heights[i]
            key_name = names[i]
            j = i - 1

            # Move elements of heights and names that are less than key_height
            while j >= 0 and key_height > heights[j]:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            
            # Place the key at its correct position
            heights[j + 1] = key_height
            names[j + 1] = key_name
        
        return names