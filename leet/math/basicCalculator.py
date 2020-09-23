class Solution:
    def calculate(self, s: str) -> int:
        s += '$'
        def helper(stk, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                elif c.isdigit():
                    num = num * 10 + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i+1)
                else:
                    if sign == '+':
                        stk.append(num)
                    if sign == '-':
                        stk.append(-num)
                    sign = c
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stk), i
                
            return sum(stk)
            
        return helper([],0)