class Solution:
    def removeVowels(self, S: str) -> str:
        vw = set('aeiou')
        return "".join([c for c in S if c not in vw])


    def removeVowels(self, S):str
        return re.sub('a|e|i|o|u', '', S)