# Title: Insert Interval
# Runtime: 100 ms
# Memory: 17.4 MB

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = collections.deque([])
        def areOverlapping(currentInterval: List[int], newInterval: List[int]) -> bool:
            return newInterval[0] <= currentInterval[1] and newInterval[1] >= currentInterval[0]
        
        def isBefore(currentInterval: List[int], newInterval: List[int]) -> bool:
            return newInterval[0] < currentInterval[0]
        
        def mergeIntervals(currentInterval: List[int], newInterval: List[int]) -> List[int]:
            return [min(currentInterval[0], newInterval[0]), max(currentInterval[1], newInterval[1])]
        
        flag = False
        for i in range(len(intervals)):
            if areOverlapping(intervals[i], newInterval):
                newIntervals.append(mergeIntervals(intervals[i], newInterval))
                for j in range(i + 1, len(intervals)):
                    if areOverlapping(newIntervals[-1], intervals[j]):
                        lastInterval = newIntervals.pop()
                        newIntervals.append(mergeIntervals(lastInterval, intervals[j]))
                    else:
                        newIntervals.append(intervals[j])
                flag = True
                break
                
            if isBefore(intervals[i], newInterval):
                newIntervals.append(newInterval)
                newIntervals.append(intervals[i])
                for j in range(i + 1, len(intervals)):
                    newIntervals.append(intervals[j])
                flag = True
                break    
            newIntervals.append(intervals[i])
        if not flag:
            newIntervals.append(newInterval)
        return list(newIntervals)
                
        