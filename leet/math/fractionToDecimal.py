class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        n,r = divmod(abs(numerator), abs(denominator))
        res = []
        remainders = {}
        
        if numerator * denominator < 0:
            res.append('-')
                
        res.append(str(n))
        
        if r > 0:
            res.append(".")
        
        while r > 0 and r not in remainders:
            remainders[r] = len(res)
            r *= 10
            n, r = divmod(r, abs(denominator))
            res.append(str(n))
        
        if r in remainders:
            idx = remainders[r]
            res.insert(idx,'(')
            res.append(')')
        
        return "".join(res)