class Solution:
    def toHex(self, num: int) -> str:
        n = num
        rtn = []
        index  = "0123456789abcdef"
        
        if n == 0:
            return '0'
        
        if n < 0:
            n += 2 ** 32
            
        while n > 0:
            digit = n % 16
            n = n // 16
            rtn.append(index[digit])
        
        return "".join(rtn[::-1])