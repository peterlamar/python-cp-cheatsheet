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

class Solution:
    def generateParenthesis(self, n:int) -> List[str]:
        rtn = []
        
        def dfs(left:int, right:int, s:str):
            if (len(s) == 2*n):
                rtn.append(s)
                return
            if left > 0:
                dfs(left-1,right+1,s+'(')
            if right > 0:
                dfs(left,right-1,s+')')
        
        dfs(n,0,"")
        return rtn