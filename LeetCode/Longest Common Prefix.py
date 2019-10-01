# Title: Longest Common Prefix
# Runtime: 64 ms
# Memory: 13.8 MB

# Time Complexity: O(nm) where n is the number of strings and m is the length of the longest string
# Space Complexity: O(1)
class Solution:
    def commonPrefix(self, first: str, second: str) -> str:
        lcp = ""
        for i in range(min(len(first), len(second))):
            if first[i] == second[i]:
                lcp += first[i]
            else:
                break
        return lcp
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        lcp = self.commonPrefix(strs[0], strs[1])
        for i in range(2, len(strs)):
            lcp = self.commonPrefix(strs[i], lcp)
        return lcp
            