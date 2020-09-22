"""
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 0:
            return []
        
        self.ans = []
        
        def dfs(idx, path):
            if idx == len(num) - 1:
                path += num[idx]
                if eval(path) == target:
                    self.ans.append(path)
                return
            
            dfs(idx + 1, path + num[idx] + "+")
            dfs(idx + 1, path + num[idx] + "-")
            dfs(idx + 1, path + num[idx] + "*")
            if (num[idx] != '0' or (path and path[-1] not in ['-','+','*'] and num[idx]=='0')):
                dfs(idx + 1, path + num[idx])

        
        dfs(0, "")
        
        return self.ans

class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        ans = []
        
        def dfs(i, prev, cur, val, eq):
            if i == len(num):
                if val == target and cur == 0:
                    ans.append("".join(eq[1:]))
                return
            
            cur = cur *10 + int(num[i])
            str_op = str(cur)
            
            if cur > 0:
                dfs(i+1, prev, cur, val, eq)
            
            dfs(i+1, cur, 0, val + cur, eq + "+" + str_op)
            
            if eq:
                dfs(i+1, -cur, 0, val - cur, eq + '-' + str_op) 
                dfs(i+1, cur * prev, 0, val - prev + (cur*prev), eq + '*' + str_op) 

        
        dfs(0,0,0,0,"")
        
        return ans
            