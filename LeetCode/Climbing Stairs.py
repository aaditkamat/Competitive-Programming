# Title: Climbing Stairs
# Runtime: 32 ms
# Memory: 13.9 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2
        for i in range(3, n + 1, 2):
            first += second
            second += first
        return first if n % 2 == 1 else second
        