# Title: Contains Duplicate
# Runtime: 152 ms
# Memory: 20 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_store = {}
        for num in nums:
            if num in count_store:
                return True
            else:
                count_store[num] = 1
        return False