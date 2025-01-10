# https://leetcode.com/problems/word-subsets

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Step 1: Create a universal count for all characters in words2
        universal_count = Counter()
        
        for b in words2:
            bcnt = Counter(b)
            # Update the universal count with the maximum frequency of each character
            for char, count in bcnt.items():
                universal_count[char] = max(universal_count[char], count)

        ans = []
        # Step 2: Check each word in words1 against the universal count
        for a in words1:
            acnt = Counter(a)
            # Check if a contains all characters in the universal count with required frequencies
            if all(acnt[char] >= count for char, count in universal_count.items()):
                ans.append(a)

        return ans
