class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rtn = []
        
        for i, l in enumerate(zip(*strs)):
            if len(set(l)) == 1:
                rtn.append(l[0])
            else:
                break
        
        return "".join(rtn)