class Solution:
    def isNumber(self, s: str) -> bool:
        met_e = met_p = met_d = False
        
        s = s.strip()
        
        for i, c in enumerate(s):
            if c == 'e':
                if met_e or met_d == False:
                    return False
                met_e = True
                met_d = False
            elif c == '-' or c == '+':
                if i > 0 and s[i-1] != 'e':
                    return False
            elif c == '.':
                if met_p or met_e:
                    return False
                met_p = True
            elif c.isdigit():
                met_d = True
            else:
                return False
        
        return met_d
                
                