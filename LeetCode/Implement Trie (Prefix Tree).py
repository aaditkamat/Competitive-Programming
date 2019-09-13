# Title: Implement Trie (Prefix Tree)
# Runtime: 320 ms
# Memory: 35 MB

class TrieNode:
    def __init__(self, index):
        self.index = index
        self.children = {}

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(-1)
        

    def recursiveInsert(self, word: str, curr: TrieNode):
        if curr.index == len(word) - 1:
            if '' not in curr.children:
                curr.children[''] = TrieNode(curr.index + 1)
            return
        if word[curr.index + 1] not in curr.children:
            curr.children[word[curr.index + 1]] = TrieNode(curr.index + 1)
        self.recursiveInsert(word, curr.children[word[curr.index + 1]])
        
    def recursiveSearch(self, word: str, curr: TrieNode):
        if curr.index == len(word) - 1:
            return '' in curr.children
        if word[curr.index + 1] not in curr.children:
            return False
        return self.recursiveSearch(word, curr.children[word[curr.index + 1]])
    
    def recursiveStartsWith(self, word: str, curr: TrieNode):
        if curr.index == len(word) - 1:
            return True
        if word[curr.index + 1] not in curr.children:
            return False
        return self.recursiveStartsWith(word, curr.children[word[curr.index + 1]])
    
                    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.recursiveInsert(word, self.root)
        
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.recursiveSearch(word, self.root)
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.recursiveStartsWith(prefix, self.root)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)