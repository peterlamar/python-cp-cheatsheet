"""
Basic Calculator II
"""
class Solution:
    def calculate(self, s: str) -> int:
        s += '$'
        sign = '+'
        i = num = 0
        stk = []
        
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            elif c.isdigit():
                num = num * 10 + int(c)
                i += 1
            else:
                if sign == '+':
                    stk.append(num)
                if sign == '-':
                    stk.append(-num)
                if sign == '*':
                    stk.append(stk.pop() * num)
                if sign == '/':
                    stk.append(int(stk.pop() / num))
                
                sign = c
                num = 0
                i += 1
        
        return sum(stk)
        