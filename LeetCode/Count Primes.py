# Title: Count Primes
# Runtime: 2032 ms
# Memory: 25.5 MB

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        sieve = [True] * (n - 2)
        ctr, start = 0, 2
        for i in range(len(sieve)):
            if sieve[i]:
                j = 2
                while (i + 2) * j <= len(sieve) + 1:
                    sieve[(i + 2) * j - 2] = False
                    j += 1
                ctr += 1
        return ctr
            
            
        