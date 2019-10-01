# Title: Maximum Number of Balloons
# Runtime: 32 ms
# Memory: 13.9 MB

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def get_mapping(string: str) -> dict:
            mapping = {}
            for char in string:
                if char in mapping:
                    mapping[char] += 1
                else:
                    mapping[char] = 1
            return mapping 
        
        mapping_text = get_mapping(text)
        mapping_balloon = get_mapping("balloon")
        result = []
        for char, occurences in mapping_balloon.items():
            if char not in mapping_text or mapping_text[char] < occurences:
                return 0
            result.append(mapping_text[char] // occurences)
        return min(result)
                
            
        