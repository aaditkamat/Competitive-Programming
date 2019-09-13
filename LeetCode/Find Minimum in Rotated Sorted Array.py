# Title: Find Minimum in Rotated Sorted Array
# Runtime: 48 ms
# Memory: 14 MB

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid == end or (nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[-1] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1