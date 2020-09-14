class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        """
        """
        """
        time: c in word
        space: c
        """
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie 
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        
        node['$'] = True

        """
        time: c in word
        space: 1
        """
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie 
        
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        
        return '$' in node
        
        """
        time: c in prefix
        space: 1
        """
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie 

        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)