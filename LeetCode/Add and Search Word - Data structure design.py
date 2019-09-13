# Title: Add and Search Word - Data structure design
# Runtime: 360 ms
# Memory: 31.8 MB

class TrieNode:
    def __init__(self):
        self.children = {}
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for index in range(len(word)):
            if word[index] not in curr.children:
                curr.children[word[index]] = TrieNode()
            if word == "ab":
                print(curr.children)
            curr = curr.children[word[index]]
        curr.children[''] = TrieNode()
        if word == "ab":
            print(curr.children)

    def checkAll(self, word: str, index: int, curr: TrieNode) -> bool:
        if index == len(word):
            return '' in curr.children
        if word[index] == '.':
            for child in curr.children.values():
                if self.checkAll(word, index + 1, child):
                    return True
            return False
        if word[index] not in curr.children:
            return False
        return self.checkAll(word, index + 1, curr.children[word[index]])
    
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.root
        for index in range(len(word)):
            if word[index] == '.':
                for child in curr.children.values():
                    if self.checkAll(word, index + 1, child):
                        return True
                return False
            if word[index] not in curr.children:
                return False
            curr = curr.children[word[index]]
        return '' in curr.children


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)