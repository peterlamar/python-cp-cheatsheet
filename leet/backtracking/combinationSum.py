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