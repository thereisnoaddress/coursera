"""
Leetcode 676 Magic Dictionary implemented in two ways:
First, implemented as a Trie
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
    
    """
    Recursive function
        - if the word is empty, check if all chances have been used up and whether it's at the end
        - check whether word initial matches with one of the keys; if so, continue to next char
            - if word initial doesn't match up with one of the keys, use up a chance (assume that char is being substituted)
            - continue searching but with 0 chances left
    """
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
################################### Done using dictionary -- more intuitive

class MagicDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lengthDict = {}
        # key: length -> value: String[]

    def buildDict(self, dictionary) -> None:
        # put words with the same length together in a dictionary
        for word in dictionary: 
            length = len(word)
            if length not in self.lengthDict: 
                self.lengthDict[length] = [word]
            else: 
                self.lengthDict[length].append(word)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.lengthDict: return False
        words = self.lengthDict[len(searchWord)]
        
        for word in words: 
            diff = 0
            for i in range(len(word)): 
                if word[i] != searchWord[i]:
                    diff += 1
            if diff == 1: 
                return True
        return False