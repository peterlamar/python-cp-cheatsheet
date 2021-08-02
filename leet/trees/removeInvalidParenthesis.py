class Solution:
    """
    time: 14 min
    time: O(2^n)
    space: O(n)
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def isValid(s) -> bool:
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    if cnt == 0:
                        return False
                    else:
                        cnt -= 1
            return cnt == 0
            
        
        rtn = []
        
        level = set()
        level.add(s)
        
        while True:
            # check if string is valid, if so then add to rtn
            for s in level:
                if isValid(s):
                    rtn.append(s)
                    
            if len(rtn) > 0:
                return rtn
            
            # if not, make substrings and repeat
            newLevel = set()
            for s in level:
                for i,c in enumerate(s):
                    if c == '(' or ')':
                        newLevel.add(s[0:i] + s[i+1:len(s)])
            level = newLevel



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