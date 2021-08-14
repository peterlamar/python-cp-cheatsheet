class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        rk = { v:[0] * len(votes[0]) + [v] for v in votes[0]}
        for v in votes:
            for i, c in enumerate(v):
                rk[c][i] -= 1
        
        rtn = sorted(votes[0], key=lambda x: rk[x])
        return "".join(rtn)