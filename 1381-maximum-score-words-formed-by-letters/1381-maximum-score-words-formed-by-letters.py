class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_count = Counter(letters)  
        
        def word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)  
        
        def can_form(word, count):
            word_count = Counter(word)
            for c in word_count:
                if word_count[c] > count[c]:
                    return False
            return True
        
        def backtrack(index, current_score):
            if index == len(words):
                return current_score
            
            # Skip the current word
            max_score = backtrack(index + 1, current_score)
            
            # Include the current word if possible
            if can_form(words[index], letter_count):
                # Update letter count
                for c in words[index]:
                    letter_count[c] -= 1
                
                # Calculate new score
                new_score = current_score + word_score(words[index])
                
                # Recur to the next word
                max_score = max(max_score, backtrack(index + 1, new_score))
                
                # Backtrack: Restore letter count
                for c in words[index]:
                    letter_count[c] += 1
            
            return max_score
        
        return backtrack(0, 0)