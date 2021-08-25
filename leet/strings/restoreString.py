class Solution:
    # Shuffle String
    def restoreString(self, s: str, indices: List[int]) -> str:
        # BF, assign to new array
        rtn = [""] * len(s)
        
        for i, ic in enumerate(indices):
            rtn[ic] = s[i]
            
        return "".join(rtn)