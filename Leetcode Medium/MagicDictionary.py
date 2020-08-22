"""
Leetcode 676 Magic Dictionary implemented in two ways
"""

class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.isEnd = False

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def addWord(self, word): 
        curNode = self.root
        for char in word: 
            if char not in curNode.children: 
                curNode.children[char] = TrieNode()
            curNode = curNode.children[char]
        
        curNode.isEnd = True

    def buildDict(self, dictionary):
        for word in dictionary: 
            self.addWord(word)
    

    def newSearch(self, chances, node, word): 
        if not word: 
            return chances == 0 and node.isEnd
        
        for key in node.children.keys(): 
            if word[0] == key: 
                if self.newSearch(chances, node.children[key], word[1:]): 
                    return True
            elif chances == 1: 
                if self.newSearch(0, node.children[key], word[1:]): 
                    return True
        return False
    
    def search(self, searchWord: str) -> bool:
        curNode = self.root
        return self.newSearch(1, curNode, searchWord)
        
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)