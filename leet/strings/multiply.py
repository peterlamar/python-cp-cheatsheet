class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        carry2 = 1
        rtn = 0
        
        for n1 in num1[::-1]:
            carry1 = 1
            for n2 in num2[::-1]:
                d1 = ord(n1) - ord('0')
                d2 = ord(n2) - ord('0')
                rtn += d1*d2*carry1*carry2
                carry1 *= 10
            carry2 *= 10
        
        return str(rtn)