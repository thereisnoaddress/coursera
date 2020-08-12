"""
Leetcode 211
https://leetcode.com/problems/add-and-search-word-data-structure-design/
"""


class TrieNode():

    def __init__(self): 
        self.children = {}
        self.complete = False


class WordDictionary:

    def __init__(self):
        """
        Basically a Trie
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curNode = self.root
        
        for char in word: 
            if char not in curNode.children:
                curNode.children[char] = TrieNode()
            curNode = curNode.children[char]
        
        curNode.complete = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.res = False
        self.dfs_search(word, node)
        return self.res
        
    def dfs_search(self, word, root): 
        
        if not word: 
            if root.complete:
                self.res = True
            return 
        
        if word[0] == '.': 
            for val in root.children.values(): 
                self.dfs_search(word[1:], val)
        else:
            node = root.children.get(word[0])
            if not node:
                return 
            self.dfs_search(word[1:], node)
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)