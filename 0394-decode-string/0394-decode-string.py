"""class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                curr = ''
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop() # remove the [
                
                x = ''
                while stack and stack[-1].isdigit():
                    x = stack.pop() + x
                
                stack.append(curr * int(x))

        return ''.join(stack)

"""
class Solution:
    def decodeString(self, s: str) -> str:
        def decode(index):
            result = ''
            num = 0
            
            while index < len(s):
                char = s[index]
                
                if char.isdigit():
                    # Build the number (could be more than one digit)
                    num = num * 10 + int(char)
                
                elif char == '[':
                    # Recursively decode the substring
                    index, decoded_string = decode(index + 1)
                    result += decoded_string * num  # Repeat the decoded string num times
                    num = 0  # Reset num after using it
                
                elif char == ']':
                    # Return the current result and the next index
                    return index, result
                
                else:
                    # Normal character, just add to the result
                    result += char
                
                index += 1
            
            return result
        
        # Start decoding from index 0
        return decode(0)
