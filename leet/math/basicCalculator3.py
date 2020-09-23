class Solution:
    def calculate(self, s: str) -> int:
        s += '$'
        def helper(stk, i):
            sign = '+'
            num = 0
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
                    if sign == '*':
                        stk.append(stk.pop() * num)
                    if sign == '/':
                        stk.append(int(stk.pop() / num))
                    i += 1
                    num = 0
                    if c == ')':
                        return sum(stk), i
                    sign = c
            return sum(stk)
        return helper([],0)