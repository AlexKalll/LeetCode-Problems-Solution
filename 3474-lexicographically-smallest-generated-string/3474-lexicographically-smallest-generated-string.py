class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        result = ['?'] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        
        for i in range(n):
            if str1[i] == 'T':
                for k in range(m):
                    pos = i + k
                    if result[pos] == '?':
                        result[pos] = str2[k]
                        fixed[pos] = True
                    elif result[pos] != str2[k]:
                        return ""
        
        for i in range(n + m - 1):
            if result[i] == '?':
                result[i] = 'a'
        
        for i in range(n):
            if str1[i] == 'F':
                eq = True
                free_indices = []
                for k in range(m):
                    pos = i + k
                    if result[pos] != str2[k]:
                        eq = False
                        break
                    if not fixed[pos]:
                        free_indices.append(pos)
                
                if eq:
                    if not free_indices:
                        return ""
                    j = free_indices[-1]
                    changed = False
                    for c in range(ord(result[j]) + 1, ord('z') + 1):
                        if chr(c) != str2[j - i]:
                            result[j] = chr(c)
                            changed = True
                            break
                    if not changed:
                        return ""
        
        return ''.join(result)
