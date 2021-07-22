
"""
time: O(M + N) N is 26 (Letters) so just O(M)
space: O(1)
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        al = {}
        
        for i, c in enumerate(order):
            al[c] = i
         
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for c1, c2 in zip(a,b):
                if al[c1] > al[c2]:
                    return False
                elif al[c1] < al[c2]:
                    break
        
        return True

"""
time: O(n)
space: O(1)
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dct = {}
        
        for i, c in enumerate(order):
            dct[c] = i
        
        trans = lambda x: [dct[c] for c in x]
        
        for w1, w2 in zip(words, words[1:]):
            if trans(w1) > trans(w2):
                return False
        
        return True

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dt = {c:i for i,c in enumerate(order)}
        
        trans = lambda x: [dct[c] for c in x]
        
        for w1, w2 in zip(words, words[1:]):
            if trans(w1) > trans(w2):
                return False
        
        return True