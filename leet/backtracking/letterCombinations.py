class Solution:
    ref = ["", "", "abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits:str) -> list[str]:
        rtn = []
        if len(digits) == 0: return rtn
        self.backtracking(rtn, digits, "", 0)
        return rtn
    
    def backtracking(self, rtn:list, digits:str, tmp:str, idx:int):
        if len(tmp) == len(digits):
            rtn.append(tmp)
            return
        
        num = ord(digits[idx]) - ord('0')
        letters = self.ref[num]
        for i in range(0, len(letters)):
            self.backtracking(rtn, digits, tmp + letters[i], idx+1)

class Solution:
    ref = {"2":"abc","3":"def","4":"ghi","5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz"}
    
    def letterCombinations(self, digits):
        rtn = []
        if len(digits)==0:return rtn
        self.backtracking(rtn, digits, "", 0)
        
        return rtn
    
    def backtracking(self, rtn, digits, tmp, idx):
        if (len(tmp)==len(digits)):
            rtn.append(tmp)
            return
        
        key = digits[idx]
        letters = self.ref[key]
        for c in letters:
            self.backtracking(rtn, digits, tmp + c, idx+1)