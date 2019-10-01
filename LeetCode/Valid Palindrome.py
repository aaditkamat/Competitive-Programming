# Title: Valid Palindrome
# Runtime: 60 ms
# Memory: 14.2 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        allowed = string.ascii_letters + string.digits
        while start < end:
            if s[start] not in allowed:
                start += 1
                continue
            if s[end] not in allowed:
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
        