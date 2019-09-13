# Title: Valid Parentheses
# Runtime: 36 ms
# Memory: 13.9 MB

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = [')', '}', ']']
        opening = ['(', '{', '[']
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) > 0:
                    compare_char = stack.pop()
                    if not closing.index(char) == opening.index(compare_char):
                        return False
                else:
                    return False
        return len(stack) == 0
            
        