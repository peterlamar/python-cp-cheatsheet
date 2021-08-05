class WordDictionary:

    def __init__(self):
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        node = self.trie 
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True
    """
    time: c
    space: c
    time: c * Nodes in c for .s
    space: 1, n for .s (recursion)
    """
    def search(self, word: str) -> bool:
        node = self.trie
        def searchNode(word, node):
            for i,c in enumerate(word):
                if c in node:
                    node = node[c]
                elif c == '.':
                    return any(searchNode(word[i+1:], node[cn]) for cn in node if cn != '$' )
                else:
                    return False
            return '$' in node
        return searchNode(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)