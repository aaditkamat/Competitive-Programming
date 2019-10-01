# Title: Move Zeroes
# Runtime: 60 ms
# Memory: 15.2 MB

#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums: List[int], j: int, k: int) -> None:
            temp = nums[j]
            nums[j] = nums[k]
            nums[k] = temp
            
        dst = 0
        for i in range(len(nums)):
            if nums[i]:
                swap(nums, dst, i)
                dst += 1