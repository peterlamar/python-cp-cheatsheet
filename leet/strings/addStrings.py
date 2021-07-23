class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        rtn = []
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        
        carry = 0
        while n1 >= 0 and n2 >= 0:
            d1 = ord(num1[n1]) - ord('0')
            d2 = ord(num2[n2]) - ord('0')
            sum = d1 + d2 + carry
            carry = sum // 10
            digit = sum % 10
            rtn.append(chr(digit + ord('0')))
            n1 -= 1
            n2 -= 1
            
        while n1 >= 0:
            d1 = ord(num1[n1]) - ord('0')
            sum = d1 + carry
            carry = sum // 10
            digit = sum % 10
            rtn.append(chr(digit + ord('0')))
            n1 -= 1

        while n2 >= 0:
            d1 = ord(num2[n2]) - ord('0')
            sum = d1 + carry
            carry = sum // 10
            digit = sum % 10
            rtn.append(chr(digit + ord('0')))
            n2 -= 1
        
        if carry:
            rtn.append(carry)
        
        
    
        return "".join(str(x) for x in rtn[::-1])


class Solution:
    def addStrings2(self, num1: str, num2: str) -> str:
        rtn = []
        
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        
        carry = 0
        while n1 >= 0 or n2 >= 0:
            d1 = 0
            d2 = 0
            if n1 >= 0: d1 = ord(num1[n1]) - ord('0')
            if n2 >= 0: d2 = ord(num2[n2]) - ord('0')
            total = d1 + d2 + carry
            carry = total // 10
            digit = total % 10
            rtn.append(chr(digit + ord('0')))
            n1 -= 1
            n2 -= 1
        
        if carry > 0:
            rtn.append(chr(carry + ord('0')))
        
        return "".join(rtn[::-1])

    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        rtn = deque()
        carry = 0
        
        while num1 or num2:
            n1 = ord(num1.pop()) - ord('0') if num1 else 0
            n2 = ord(num2.pop()) - ord('0') if num2 else 0
            tmp = n1 + n2 + carry
            digit = tmp % 10
            carry = tmp // 10
            rtn.appendleft(digit)
        
        if carry > 0:
            rtn.appendleft(carry)
        
        return "".join([str(i) for i in rtn])