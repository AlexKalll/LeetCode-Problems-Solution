from collections import defaultdict
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = defaultdict(int)
        
        for char in chars:
            chars_count[char] += 1
        
        total_length = 0

        for word in words:
            word_count = defaultdict(int)
            can_form = True  # kinda flag
            
            for char in word:
                word_count[char] += 1
                if word_count[char] > chars_count[char]:
                    can_form = False
                    break
            
            if can_form:
                total_length += len(word)
        
        return total_length
