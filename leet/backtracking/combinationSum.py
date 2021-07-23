class Solution:
    def combinationSum(self, cand, target):
        rtn = []
        
        def backtracking(cand, target, tmp:List[int]):
            if target == 0:
                rtn.append(tmp)
            if target < 0:
                return
            for i in range(len(cand)):
                # cand[i:] factorial comb trick
                backtracking(cand[i:], target-cand[i], tmp + [cand[i]])
        
        backtracking(cand, target, [])
        return rtn

class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        rtn = []
        
        def dfs(path:List[int], remain:int, tmp:List[int]):
            if remain < 0:
                return
            if remain == 0:
                rtn.append(tmp)
                return
            
            for i in range(0, len(path)):
                dfs(path[i:], remain-path[i], tmp + [path[i]])
                
        dfs(cand, target, [])
            
        return rtn
        