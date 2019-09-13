# Title: Top K Frequent Elements
# Runtime: 124 ms
# Memory: 18.2 MB

class Solution:
    def getEleToFreqMapping(self, nums: List[int]) -> dict:
        mapping = {}
        for num in nums:
            if num in mapping:
                mapping[num] -= 1
            else:
                mapping[num] = -1
        return mapping
    
    def getFreqToEleMapping(self, nums: List[int]) -> dict:
        eleToFreqMapping = self.getEleToFreqMapping(nums)
        freqToEleMapping = {}
        for element, frequency in eleToFreqMapping.items():
            if frequency in freqToEleMapping:
                freqToEleMapping[frequency].append(element)
            else:
                freqToEleMapping[frequency] = [element]
        return freqToEleMapping
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqToEleMapping = self.getFreqToEleMapping(nums)
        frequencies = list(freqToEleMapping.keys())
        heapq.heapify(frequencies)
        mostFrequent = []
        ctr = 0
        while ctr < k:
            frequency = heapq.heappop(frequencies)
            mostFrequent.extend(freqToEleMapping[frequency])
            ctr += len(freqToEleMapping[frequency])
        return mostFrequent[0: k]
            
        