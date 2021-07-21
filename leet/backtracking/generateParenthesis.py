class Solution:

    def generateParenthesis(self, n:int) -> list[str]:
        stk = []
        self.backtracking(stk, n, n, 0, "")
        return stk
    
    def backtracking(self, stk:list, n:int, left:int, right:int, s:str):
        if len(s) == 2*n:
            stk.append(s)
            return
        if left > 0:
            self.backtracking(stk, n, left-1, right+1, s + "(")
        if right > 0:
            self.backtracking(stk, n, left, right-1, s + ")")    
