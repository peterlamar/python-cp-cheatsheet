class Solution:
    """
    time: 14 min
    time: O(n * 2^(n-1))
    space: O(n)
    """
    def isValid(self, s) -> bool:
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        rtn = []
        v = set()
        v.add(s)
        
        if len(s) == 0: return [""]
                
        while True:
            for n in v:
                if self.isValid(n):
                    rtn.append(n)
            
            if len(rtn) > 0:
                break
            
            # add children to set
            level = set()
            for n in v:
                for i, c in enumerate(n):
                    if c == '(' or c == ')':
                        sub = n[0:i] + n[i + 1:len(n)]
                        level.add(sub)
            v = level
        return rtn



    def removeInvalidParentheses(self, s: str) -> List[str]:
        # initialize a set with one element
        # set is used here in order to avoid duplicate element
        level = {s}
        while True:
            valid = []
            for elem in level:
                if self.isValid(elem):
                    valid.append(elem)
            if valid:
                return valid
            # initialize an empty set
            new_level = set()
            # BFS
            for elem in level:
                for i in range(len(elem)):
                    new_level.add(elem[:i] + elem[i + 1:])
            level = new_level
    
    def isValid(self,s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0


def removeInvalidParentheses(self, s):
    def isvalid(s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr += 1
            elif c == ')':
                ctr -= 1
                if ctr < 0:
                    return False
        return ctr == 0
    level = {s}
    while True:
        valid = filter(isvalid, level)
        if valid:
            return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}