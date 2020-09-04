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
        al = {}
        
        for i, c in enumerate(order):
            al[c] = i
         
        trans = lambda x: list(al[i] for i in x)
        """
        for i in range(len(words) - 1):
            if trans(words[i+1]) < trans(words[i]):
                return False
        """
        return all(trans(words[i+1]) >= trans(words[i]) for i in range(len(words)-1))