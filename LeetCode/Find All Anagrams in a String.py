# Title: Find All Anagrams in a String
# Runtime: 148 ms
# Memory: 14.7 MB

# Time Complexity: O(mn) where m is length of s and n is length of p
# Space Complexity: O(m + n) 

class Solution:
    def decrementCount(self, charMap: dict, char: str):
        charMap[char] -= 1
        if not charMap[char]:
            del charMap[char]
            
    def incrementCount(self, charMap: dict, char: str):
        if char in charMap:
            charMap[char] += 1
        else:
            charMap[char] = 1
            
    def getCharMap(self, string: str) -> dict:
        charMap = {}
        for char in string:
            self.incrementCount(charMap, char)
        return charMap
   
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        sCharMap, pCharMap = self.getCharMap(s[0: len(p)]), self.getCharMap(p)
        indiceList = []
        for i in range(0, len(s) - len(p) + 1):
            if sCharMap == pCharMap:
                indiceList.append(i)
            self.decrementCount(sCharMap, s[i])
            if i < len(s) - len(p):
                self.incrementCount(sCharMap, s[i + len(p)])
        return indiceList
        