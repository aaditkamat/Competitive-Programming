# Title: Diet Plan Performance
# Runtime: 288 ms
# Memory: 23.4 MB

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        count = 0
        window = sum(calories[0: k])       
        if window < lower:
            count -= 1
        elif window > upper:
            count += 1
        for i in range(1, len(calories) - k + 1):
            window -= calories[i - 1]
            window += calories[i + k - 1]
            print(window)
            if window < lower:
                count -= 1
            elif window > upper:
                count += 1
        return count