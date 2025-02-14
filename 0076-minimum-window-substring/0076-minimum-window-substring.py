from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        window_dict = defaultdict(int)
        solution = (float('-inf'), float('inf'))
        
        required = len(dict_t)
        acquired = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_dict[char] += 1

            if char in dict_t and window_dict[char] == dict_t[char]:
                acquired += 1
            
            while acquired == required:
                if solution[1] - solution[0] > right - left:
                    solution = (left, right)

                left_char = s[left]
                window_dict[left_char] -= 1

                if left_char in dict_t and window_dict[left_char] < dict_t[left_char]:
                    acquired -= 1

                left += 1

        if solution[0] == float('-inf'):
            return ""
        else:
            return s[solution[0]:solution[1] + 1]
