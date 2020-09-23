class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        while tokens:
            c = tokens.pop(0)
            if c not in '+-/*':
                stk.append(int(c))
            else:
                a = stk.pop()
                b = stk.pop()
                
                if c == '+':
                    stk.append(a + b)
                if c == '-':
                    stk.append(b-a)
                if c == '*':
                    stk.append(a * b)
                if c == '/':
                    stk.append(int(b / a))
                    
        return stk[0]