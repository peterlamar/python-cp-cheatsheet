class Solution:
    def lengthLongestPath(self, input: str) -> int:

        lvlCnt = {-1:0}
        rtn = 0
        
        # keep count of last level, maxLen
        for s in input.split('\n'):
            level = s.count('\t')
            lvlCnt[level] = len(s) + lvlCnt[level-1] - level
            
            if '.' in s:
                rtn = max(rtn, lvlCnt[level]+level)
            
        return rtn