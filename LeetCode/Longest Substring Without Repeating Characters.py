# Title: Longest Substring Without Repeating Characters
# Runtime: 76 ms
# Memory: 14.1 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, start, store = 0, 0, {}
        for curr in range(len(s)):
            char = s[curr]
            if char in store:
                new_start = store[char] + 1
                for prev in range(start, new_start):
                    del store[s[prev]]
                start = new_start
            store[char] = curr
            count = max(count, curr - start + 1)
        return count