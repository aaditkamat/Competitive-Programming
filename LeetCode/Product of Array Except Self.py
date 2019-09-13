# Title: Product of Array Except Self
# Runtime: 140 ms
# Memory: 20.8 MB

class Solution:
    def get_left_products(self, nums: List[int]) -> List[int]:
        curr_prod = 1
        left_prod = []
        for num in nums[: : -1]:
            left_prod.append(curr_prod * num)
            curr_prod *= num
        left_prod.reverse() 
        left_prod.append(1)
        return left_prod

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = self.get_left_products(nums)
        curr_prod = 1
        result = []
        for i in range(len(nums)):
            result.append(left_prod[i + 1] * curr_prod)
            curr_prod *= nums[i]
        return result
        