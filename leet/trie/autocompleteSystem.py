class Trie:
    def __init__(self):
        self.root = {}
    
    def addWord(self, s: str):
        tmp = self.root 
        for c in s:
            if c not in tmp:
                tmp[c] = {}
            tmp = tmp[c]
        tmp['#'] = s # Store full word at '#' to simplify
    
    def matchPrefix(self, s: str, tmp=None):
        if not tmp: tmp = self.root 
        for c in s:
            if c not in tmp:
                return []
            tmp = tmp[c]
        
        rtn = []
        
        for k in tmp:
            if k == '#':
                rtn.append(tmp[k])
            else:
                rtn += self.matchPrefix('', tmp[k])
        return rtn
                

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        
        self.trie = Trie()
        self.cnt = collections.Counter()
        self.userKeys = ""
        for i, w in enumerate(sentences):
            self.trie.addWord(w)
            self.cnt[w] = times[i]
        
    def input(self, c: str) -> List[str]:
        
        if c != '#':
            self.userKeys += c
            # Get list of correct strings
            matches = self.trie.matchPrefix(self.userKeys)
            # sort list by rank, then abc
            return sorted(matches, key= lambda x: (-self.cnt[x], x))[:3]
        else:
            self.trie.addWord(self.userKeys)
            self.cnt[self.userKeys] += 1
            self.userKeys = ""


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)