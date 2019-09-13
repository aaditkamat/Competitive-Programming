# Title: Prime Arrangements
# Runtime: 36 ms
# Memory: 13.9 MB

class Solution:
    def factorial(self, n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    def isPrime(self, n: int) -> int:
        if n == 2:
            return True
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if not n % i:
                return False
        return True
                       
    def calculateNumOfPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n + 1):
            count = count + 1 if self.isPrime(i) else count
        return count
    
    def numPrimeArrangements(self, n: int) -> int:
        numOfPrimes = self.calculateNumOfPrimes(n)
        return (self.factorial(numOfPrimes) * self.factorial(n - numOfPrimes)) % (10 ** 9 + 7)