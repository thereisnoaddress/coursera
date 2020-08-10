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
        self.complete = False
        self.children = {}
        self.content = ""
    
    def set(self, content): 
        self.content = content

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curNode = self
        
        for char in word: 
            if char not in curNode.children: 
                newNode = Trie()
                newNode.set(char)
                curNode.children[char] = newNode
                curNode = newNode
            else: 
                curNode = curNode.children[char]
        curNode.complete = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curNode = self
        
        for char in word: 
            if char not in curNode.children: 
                return False
            curNode = curNode.children[char]
        
        return curNode.complete
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        curNode = self
        
        for char in prefix: 
            if char not in curNode.children: 
                return False
            curNode = curNode.children[char]
        
        return True
        

            



# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":    
    word = "apple"
    obj = Trie()
    obj.insert(word)
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.startsWith("app"))
    print(obj.children['a'].children['p'].children['p'].children, obj.children['a'].children['p'].children['p'].complete)
    obj.insert("app")
    print(obj.children['a'].children['p'].children['p'].complete)
    print(obj.search("app"))
  
