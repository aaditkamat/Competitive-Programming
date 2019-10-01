# Title: Plus One
# Runtime: 44 ms
# Memory: 13.9 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == [0]:
            return [1]
        currNum = int("".join(map(str, digits)))
        return list(str(currNum + 1))
        