# Title: Defanging an IP Address
# Runtime: 36 ms
# Memory: 13.8 MB

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub("\.", "[.]", address)