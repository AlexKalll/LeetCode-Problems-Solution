class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Initialize an empty list to store the indices
        indices = []
        
        # Iterate through the list of words
        for index, word in enumerate(words):
            # Check if the character x is in the current word
            if x in word:
                # Append the index to the result list
                indices.append(index)
        
        return indices