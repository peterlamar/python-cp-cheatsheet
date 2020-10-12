class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for p in path.split('/'):
            if p == '..':
                if stk:
                    stk.pop()
            elif p and p != '.':
                stk.append(p)
        return '/' + '/'.join(stk)