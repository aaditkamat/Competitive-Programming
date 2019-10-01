# Title: Single Number
# Runtime: 96 ms
# Memory: 16.3 MB

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        for num in nums:
            if mapping[num] == 1:
                return num
                
            