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

    def simplifyPath(self, path: str) -> str:
        stk = []
        p = path.split()
        
        for p in path.split('/'):
            if p == '.':
                continue
            elif p == '..':
                if stk:
                    stk.pop()
            elif len(p) > 0:
                stk.append('/' + p)
        
        if not stk:
            stk.append('/')
        
        return "".join(stk)