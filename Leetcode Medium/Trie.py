"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # maybe {firstChar: str -> words: string[]}? 
        self.words = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        prefix = word[0]
        if not self.words or not prefix in self.words: 
            self.words[prefix] = [word]
        else: 
            self.words[prefix].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word[0] in self.words: 
            return False
        else: 
            return word in self.words[word[0]]

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not self.words or prefix[0] not in self.words:
            return False
        else: 
            prefixArr = self.words[prefix[0]]
            prefixLength = len(prefix)
            for word in prefixArr: 
                if word[0:prefixLength] == prefix: 
                    return True
        return False
            



# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":    
    word = "apple"
    obj = Trie()
    obj.insert(word)
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.startsWith("app"))
    obj.insert("app")
    print(obj.search("app"))
