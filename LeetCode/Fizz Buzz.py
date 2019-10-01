# Title: Fizz Buzz
# Runtime: 52 ms
# Memory: 14.8 MB

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            string = ""
            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            if not i % 3 == 0 and not i % 5 == 0:
                string += f"{i}"
            result.append(string)
        return result