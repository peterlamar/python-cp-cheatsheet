"""
time: 6 min
erros: none!
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rtn = []
        a1 = len(a) - 1
        b1 = len(b) - 1
  
        carry = 0
        while a1 >= 0 or b1 >= 0:
            d1 = 0
            d2 = 0
            if a1 >= 0: d1 = ord(a[a1]) - ord('0')
            if b1 >= 0: d2 = ord(b[b1]) - ord('0')
            total = d1 + d2 + carry
            carry = total // 2
            digit = total % 2
            rtn.append(chr(digit + ord('0')))
            a1 -= 1
            b1 -= 1
        
        if carry:
            rtn.append(chr(carry + ord('0')))

        return "".join(rtn[::-1])

    def addBinary(self, a: str, b: str) -> str:
        rtn = deque()
        
        a = list(a)
        b = list(b)
        
        carry = 0
        while a or b:
            a1 = ord(a.pop()) - ord('0') if a else 0
            b1 = ord(b.pop()) - ord('0') if b else 0
            total = a1 + b1 + carry
            digit = total % 2
            carry = total // 2
            rtn.appendleft(str(digit))
        
        if carry:
            rtn.appendleft(str(carry))
        
        return "".join(rtn)
        
